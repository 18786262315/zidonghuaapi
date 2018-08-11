# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebOrderChangeOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_order_change_operation.xls'

    def test_orderChangeOpration(self):
        '''订单变更测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderChangeOpration')

    def test_orderChangeAuditOpration(self):
        '''订单变更审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderChangeAuditOpration')

    def test_orderTerminationOpration(self):
        '''服务终止测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTerminationOpration')

    def test_orderTerminationAuditOpration(self):
        '''服务终止审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTerminationAuditOpration')

    def test_orderCancelOpration(self):
        '''订单取消测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderCancelOpration')

if __name__ == "__main__":
    unittest.main()