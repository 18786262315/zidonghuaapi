# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBranchOrderOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_branch_order_operation.xls'

    def test_orderAppointOpration(self):
        '''预约、派单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderAppointOpration')

    def test_orderDistributionOpration(self):
        '''单个、多单派单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderDistributionOpration')

if __name__ == "__main__":
    unittest.main()