# coding: utf-8
# ----------------------------------------------
# author            : regan
# email             : x-regan@qq.com
# create at         : 2018-08-07 14:22
# last modify       : 2018-08-07 14:22
# ----------------------------------------------


from __future__ import print_function
import os
import time
import click
import logging
import logging.config
import easy_crawler
from kazoo.client import KazooClient, KazooState

from rpc_server import RequestHandler, RPCServer
from utils.misc import get_local_host, run_in_thread, available_port

from conf.config import ZK_HOSTS, ZOO_CONFIG_PROXY_PATH


logger = logging.getLogger('server')


class ZKClient(object):
    def __init__(self, zk_hosts, local_port, local_host=None,
                 server_info_path='/crawlers'):
        self.zk_hosts = zk_hosts
        self.local_host = local_host
        if not self.local_host:
            self.local_host = get_local_host()
        self.server_info_path = server_info_path
        self.server_info_znode = '{server_info_path}/{ip}:{port}'.format(
                server_info_path=server_info_path,
                ip=self.local_host,
                port=local_port)
        self.connect_zk()

    def connect_zk(self):
        self.zk = KazooClient(hosts=self.zk_hosts)
        self.zk.add_listener(self.state_listener)
        self.zk.start()

    def update_heartbeat(self):
        def callback(async_stat):
            stat = async_stat.get()
            if stat:
                _ = self.zk.set_async(self.server_info_znode, ts)
            else:
                _ = self.zk.create_async(self.server_info_znode, ts,
                                         ephemeral=True, makepath=True)
        ts = str(int(time.time()))
        async_stat = self.zk.exists_async(self.server_info_znode, watch=None)
        async_stat.rawlink(callback)

    def state_listener(self, state):
        if state == KazooState.LOST:
            # Register somewhere that the session was lost
            pass
        elif state == KazooState.SUSPENDED:
            # Handle being disconnected from Zookeeper
            pass
        else:
            self.update_heartbeat()

    def add_watcher(self, request_handler):
        @self.zk.DataWatch(ZOO_CONFIG_PROXY_PATH)
        def proxy_change(data, stat):
            run_in_thread(request_handler.config_proxy_via_zookeeper, data)

    def close(self):
        self.zk.stop()


@click.command()
@click.option('--host', default=get_local_host(),
              help='Host for service binding', show_default=True)
@click.option('--port', type=click.INT, help='Port for service binding, if not'
              ' set, will choose a available port automatic')
@click.option('--zookeeper', default=ZK_HOSTS, type=click.STRING,
              help='the zookeeper host:port', show_default=True)
@click.option('--logging-config', default=os.path.join(
              os.path.dirname(__file__), 'conf/logging.conf'),
              show_default=True, help='logging config file')
@click.option('--max-works', type=click.INT, default=100,
              help='the num of threads to deal request', show_default=True)
@click.version_option(version=easy_crawler.__version__)
def execute(**kws):
    logging.config.fileConfig(kws['logging_config'],
            disable_existing_loggers=False)
    host = kws['host']
    port = kws['port']
    if not port:
        port = available_port()
    rpc_server = RPCServer(host, port, kws['max_works'])
    request_handler = RequestHandler()
    rpc_server.start(request_handler)

    zkc = ZKClient(kws['zookeeper'], local_host=host, local_port=port)
    zkc.add_watcher(request_handler)
    try:
        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        zkc.close()
        rpc_server.stop()


if __name__ == '__main__':
    execute()
