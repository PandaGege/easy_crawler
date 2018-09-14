# coding: utf-8
# ----------------------------------------------
# author            : regan
# email             : x-regan@qq.com
# create at         : 2018-08-05 16:40
# last modify       : 2018-08-05 16:40
# ----------------------------------------------


import re
import psutil
import socket
import random

def get_local_host():
    for k, v in psutil.net_if_addrs().items():
        addr = v[0].address
        if addr.split('.')[0] in ('172', '192', '10') and \
                k.startswith('eth'):
            return addr
    return '0.0.0.0'


def available_port(ip=None, retry=100):
    if not ip:
        ip = get_local_host()

    cnt = 0
    while True:
        port = random.choice(xrange(1025, 49151))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
        except:
            return port
        finally:
            cnt += 1
            if cnt > retry:
                break


def run_in_thread(func, *args, **kwargs):
    """Run function in thread, return a Thread object"""
    from threading import Thread
    thread = Thread(target=func, args=args, kwargs=kwargs)
    thread.daemon = True
    thread.start()
    return thread


ip_patt = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|'
                     '[01]?\d\d?)$')


def check_ip(ip):
    if ip_patt.match(ip):
        return True
    return False
