# coding: utf-8
# ----------------------------------------------
# author            : regan
# email             : x-regan@qq.com
# create at         : 2018-08-11 19:49
# last modify       : 2018-08-11 19:49
# ----------------------------------------------


import random
from collections import namedtuple


_TMP = namedtuple('_', ('RANDOM', 'ROLL', 'HASH'))
BalanceMethod = _TMP(RANDOM='random',
                     ROLL='roll',
                     HASH='hash')


class LoadBalance(object):
    def __init__(self, method, nodes={}, **kws):
        if method not in BalanceMethod:
            raise ValueError('Unsupported load balancing')
        self.method = method
        self.nodes = nodes

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        if not isinstance(nodes, dict):
            return TypeError('nodes must be dict, '
                             'the value is info of the node')
        self._nodes = nodes
        self._node_key = self._nodes.keys()
        self._node_num = len(self._nodes)
        self._idx = 0

    def next(self):
        if not self._nodes:
            raise Exception('No available crawler service!')
        if self.method == BalanceMethod.RANDOM:
            node = random.choice(self._nodes.keys())
            return node, self._nodes[node]
        if self.method == BalanceMethod.ROLL:
            node = self._node_key[self._idx]
            self._idx = (self._idx + 1) % self._node_num
            return node, self._nodes[node]
