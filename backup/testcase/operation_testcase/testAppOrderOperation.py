# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppOrderOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/app_order_operation.xls'

    def test_orderOpration(self):
        '''预约、派单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderOpration')

if __name__ == "__main__":
    unittest.main()