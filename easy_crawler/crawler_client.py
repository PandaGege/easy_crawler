# coding: utf-8
# ----------------------------------------------
# author            : regan
# email             : x-regan@qq.com
# create at         : 2018-08-07 12:07
# last modify       : 2018-08-11 16:22
# ----------------------------------------------


from __future__ import print_function
import grpc
import logging
from threading import Lock
from kazoo.client import KazooClient, KazooState

from protos import crawler_pb2
from protos import crawler_pb2_grpc
from load_balancing import BalanceMethod, LoadBalance
from selector import LxmlParserDesc, JsonDesc

from utils.misc import run_in_thread, check_ip
from utils import encoding


logger = logging.getLogger(__name__)

# 貌似因为 a == b 而 hash(a) != hash(b) 的问题。
# protobuf message 被设置为了unhashable.
# 但是我们需要缓存CrawlerResponse的selector.
# 而WeakKeyDictionary的key必须是hashable的
# so启用这个内置函数，返回值为实例的内存地址
crawler_pb2.CrawlerResponse.__hash__ = lambda self: id(self)


# lazy load selector
crawler_pb2.CrawlerResponse.html_selector = LxmlParserDesc('html')
crawler_pb2.CrawlerResponse.xml_selector = LxmlParserDesc('xml')
crawler_pb2.CrawlerResponse.selector = LxmlParserDesc('html')
crawler_pb2.CrawlerResponse.json = JsonDesc()


class ZKClient(object):
    def __init__(self, zk_server, server_info_path='/crawlers'):
        self.zk_server = zk_server
        self.server_info_path = server_info_path

    def connect_zk(self):
        self.zk = KazooClient(hosts=self.zk_server)
        self.zk.add_listener(self.state_listener)
        self.zk.start()

    def state_listener(self, state):
        if state == KazooState.LOST:
            # Register somewhere that the session was lost
            pass
        elif state == KazooState.SUSPENDED:
            # Handle being disconnected from Zookeeper
            pass
        else:
            # connect, reconnect
            pass

    def add_watcher(self, rpc_client):
        @self.zk.ChildrenWatch(self.server_info_path)
        def watch_servers(children):
            run_in_thread(rpc_client._update_channels, children)

    def stop(self):
        self.zk.stop()


class RPCClient(object):
    def __init__(self, zk_server, keep_alive=False,
                 load_balancing=BalanceMethod.RANDOM):
        self.keep_alive = keep_alive
        self.load_balance = LoadBalance(load_balancing)
        self.mutex = Lock()
        self.channels = dict()
        self.zk_client = ZKClient(zk_server)
        self.zk_client.connect_zk()
        self.zk_client.add_watcher(self)

    def _update_channels(self, nodes):
        with self.mutex:
            nodes = set([node.strip() for node in nodes])
            logger.info('update nodes. now alive: %s', ','.join(nodes))
            for node in nodes:
                if node in self.channels:
                    continue
                try:
                    ip, port = node.split(':')
                    if not check_ip(ip) or not port.isdigit():
                        logger.warning('node: %s is invaild', node)
                        continue
                    logger.info('add node: %s', node)
                    if self.keep_alive:
                        channel = grpc.insecure_channel(node)
                        self.channels[node] = {'channel': channel}
                    else:
                        self.channels[node] = {}
                except Exception:
                    logger.execption('Error:')
            del_nodes = []
            for node in self.channels:
                if node not in nodes:
                    logger.info('delete node: %s, it is not available', node)
                    del_nodes.append(node)
            for node in del_nodes:
                del self.channels[node]
            self.load_balance.nodes = self.channels

    def _gen_crawler_request(self, url, **kwargs):
        req = crawler_pb2.CrawlerRequest()
        req.url = encoding.to_native_str(url, 'utf-8')
        method = kwargs.get('method', 0)
        if isinstance(method, str):
            method = {'get': 0, 'post': 1}[method.lower()]
        req.method = method
        headers = kwargs.get('headers', {})
        for k, v in headers.items():
            header = req.headers.add()
            header.key = encoding.to_native_str(k, 'utf-8')
            header.value = encoding.to_native_str(v, 'utf-8')
        req.data = encoding.to_native_str(kwargs.get('data', ''))
        req.timeout = kwargs.get('timeout', 0)
        req.max_retry = kwargs.get('max_retry', 3)
        req.allow_redirects = kwargs.get('allow_redirects', True)
        return req

    def _check_args(self, kwargs):
        for k, v in kwargs.items():
            pass

    def _choose_channel(self):
        with self.mutex:
            node, info = self.load_balance.next()
        if self.keep_alive:
            return info['channel']
        channel = grpc.insecure_channel(node)
        return channel

    def request(self, url, **kwargs):
        '''
            :type url string(utf-8)
            :type kwargs k-v:
                method: enum 0-GET, 1-POST,
                headers: k-v, <string(utf8): string(utf8)>
                data: post data; string(utf8)
                timeout: float
                max_retry: int
                allow_redirects: boolen

            rtype: CrawlerResponse
                status: enum 0-SUCCESS, 1-FAILURE
                body: html body; string(utf8)
                code: http code; int
                headers: response headers; k-v; <string(utf8): string(utf8)>
                msg: error msg; string(utf8)
                retry_num: retry num; int
                request: type of CrawlerRequest
        '''
        self._check_args(kwargs)
        req = self._gen_crawler_request(url, **kwargs)
        channel = self._choose_channel()
        stub = crawler_pb2_grpc.CrawlerStub(channel)
        response = stub.request(req)
        if not self.keep_alive:
            channel.close()
        return response

    def close(self):
        self.zk_client.close()
        with self.mutex:
            if self.keep_alive:
                for node, channel in self.channels:
                    channel.close()
