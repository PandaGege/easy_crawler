# coding: utf-8
# ----------------------------------------------
# author            : regan
# email             : x-regan@qq.com
# create at         : 2018-08-06 18:30
# last modify       : 2018-08-06 18:30
# ----------------------------------------------


from __future__ import print_function
from concurrent import futures
import time
import grpc
import random
import logging
import requests
import traceback
from protos import crawler_pb2
from protos import crawler_pb2_grpc

logger = logging.getLogger('server')


class RequestHandler(crawler_pb2_grpc.CrawlerServicer):
    def __init__(self, proxy=None):
        self.proxies = []
        self.config_proxy_via_zookeeper(proxy)

    def config_proxy_via_zookeeper(self, proxy):
        tmp = []
        if proxy:
            proxies = proxy.strip().split(';')
            for proxy in proxies:
                p = {'proxy': proxy}
                if '{random}' in proxy:
                    p['random'] = True
                tmp.append(p)
        self.proxies = tmp

    def gen_proxies(self):
        ret = {}
        if self.proxies:
            p = random.choice(self.proxies)
            proxy = p['proxy']
            if p['random']:
                ts = int(time.time()*1000)
                proxy = proxy.format(random=ts)
            ret['http'] = proxy
            ret['https'] = proxy
        return ret

    def parse_request(self, request):
        ret = {}
        url = request.url
        if not url:
            raise ValueError('request` url can`t be null')
        ret['url'] = url
        max_retry = request.max_retry
        ret['max_retry'] = max_retry if max_retry else 1
        method = request.method
        ret['method'] = 'GET' if method == 0 else 'POST'
        ret['data'] = request.data
        ret['allow_redirects'] = request.allow_redirects
        timeout = request.timeout
        ret['timeout'] = timeout if timeout else 10
        headers = {}
        for h in request.headers:
            headers[h.key] = h.value
        ret['headers'] = headers
        return ret

    def http_req(self, kwargs):
        max_retry = kwargs.pop('max_retry')
        method = kwargs.pop('method')

        retry_num = 0
        if self.proxies:
            kwargs['proxies'] = self.gen_proxies()
        while (retry_num < max_retry):
            retry_num += 1
            try:
                res = None
                if method == 'GET':
                    res = requests.get(**kwargs)
                elif method == 'POST':
                    res = requests.post(**kwargs)
                else:
                    raise ValueError('Unsupported request method:'
                                     '{}'.format(method))
                if res:
                    return True, res, retry_num
            except Exception:
                err_msg = traceback.format_exc()
        return False, err_msg, retry_num

    def request(self, request, content):
        req_args = self.parse_request(request)
        status, res, retry_num = self.http_req(req_args)

        response = crawler_pb2.CrawlerResponse()
        response.request.CopyFrom(request)
        response.retry_num = retry_num
        response.status = (1 if status else 0)
        if not status:
            response.msg = res
            return response
        response.body = res.text
        response.code = res.status_code
        for k, v in res.headers.iteritems():
            header = response.headers.add()
            header.key, header.value = k, v
        return response


class RPCServer():
    def __init__(self, host, port, max_workes=10):
        self.host = host
        self.port = port
        self.max_workes = max_workes

    def start(self, request_handler):
        self.server = grpc.server(futures.ThreadPoolExecutor(
            max_workers=self.max_workes))
        crawler_pb2_grpc.add_CrawlerServicer_to_server(request_handler,
                                                       self.server)
        self.server.add_insecure_port("{}:{}".format(self.host, self.port))
        self.server.start()

    def stop(self, grace=10):
        logger.warning('rpc server will shut down after {} seconds'.
                       format(grace))
        self.server.stop(grace)
        logger.warning('rpc server shutdown')
