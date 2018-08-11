# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testWebBasicDataOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_basic_data_operation.xls'

    def test_merchantInfoOperation(self):
        '''商家资料测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantInfoOperation')

    def test_warehouseInfoOperation(self):
        '''收货仓资料测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'warehouseInfoOperation')

    def test_trunkInfoOperation(self):
        '''物流资料测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkInfoOperation')

    def test_branchInfoOperation(self):
        '''网点资料测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'branchInfoOperation')



if __name__ == "__main__":
    unittest.main()



