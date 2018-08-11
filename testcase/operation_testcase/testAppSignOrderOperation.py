# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppSignOrderOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/app_sign_order_operation.xls'

    def test_app_sign_order_opration(self):
        '''订单签收详情测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'app_sign_order_opration')

if __name__ == "__main__":
    unittest.main()