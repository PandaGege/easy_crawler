# coding: utf-8
# ----------------------------------------------
# author            : regan
# email             : x-regan@qq.com
# create at         : 2018-08-05 17:07
# last modify       : 2018-08-05 17:07
# ----------------------------------------------

import os


LOG_CONF = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'logging.conf')

ZK_HOSTS = 'localhost:2181'


# example of the data
    # 1. socks5://host:port
    # 2. socks5h://host:port
    # 3. socks5://user:password@host:port
    # 4. socks5://user{random}:password@host:port (user=prefix+random num)
    # 5. http://host:port
    # 6. https://host:port
    # 7. none, null, '' 不使用代理

ZOO_CONFIG_PROXY_PATH = '/crawler_config/proxy'
