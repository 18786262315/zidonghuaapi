# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebFrontendOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_frontend_operation.xls'

    def test_putInStorageOpration(self):
        '''入库测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'putInStorageOpration')

    def test_outBoundOpration(self):
        '''出库测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'outBoundOpration')

    def test_orderArriveOpration(self):
        '''到件测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderArriveOpration')

    def test_trunkViolateManageOpration(self):
        '''物流违规管理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkViolateManageOpration')

if __name__ == "__main__":
    unittest.main()