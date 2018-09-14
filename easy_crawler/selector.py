# coding: utf-8
# ----------------------------------------------
# author            : regan
# email             : x-regan@qq.com
# create at         : 2018-08-12 15:05
# last modify       : 2018-08-12 15:05
# ----------------------------------------------


import json
import weakref
from lxml import etree
from StringIO import StringIO


# 因为protobuf实例(CrawlerResponse)不能添加元素
# 所以将对应的selector缓存在weakref里
# 当CrawkerReponse的实例的引用数为0的时候
# 对应的selector将被自动释放
_desc_cache = weakref.WeakKeyDictionary()


class LxmlParserDesc(object):
    '''
        parse the html page by lxml etree
    '''
    def __init__(self, which='html'):
        if which == 'html':
            self.parser = etree.HTMLParser(recover=True, encoding='utf-8')
        elif which == 'xml':
            self.parser = etree.XMLParser(recover=True, encoding='utf-8')
        else:
            raise ValueError('only support html or xml parse')
        self._attr_name = '_{}_selector'.format(which)

    def __get__(self, response, owner):
        caches = _desc_cache.setdefault(response, {})
        if self._attr_name in caches:
            return caches[self._attr_name]

        def _build_tree():
            body = response.body
            tree = etree.parse(StringIO(body), self.parser)
            return tree
        tree = _build_tree()
        caches[self._attr_name] = tree
        return caches[self._attr_name]

    def __delete__(self, response):
        del _desc_cache[response][self._attr_name]


class JsonDesc(object):
    def __get__(self, response, owner):
        caches = _desc_cache.setdefault(response, {})
        if '_json' in caches:
            return caches['_json']
        js = json.loads(response.body)
        caches['_json'] = js
        return caches['_json']

    def __delete__(self, response):
        del _desc_cache[response]['_json']
