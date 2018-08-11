# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppOrderTurnOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/app_order_turn_operation.xls'

    def test_orderTurnAuditOpration(self):
        '''转单审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTurnAuditOpration')

    def test_auditRecordOpration(self):
        '''审核记录详情测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'auditRecordOpration')

if __name__ == "__main__":
    unittest.main()