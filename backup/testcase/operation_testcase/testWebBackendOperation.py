# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBackendOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_backend_operation.xls'

    def test_orderTurnOpration(self):
        '''末端转单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderTurnOpration')

    def test_webAppointOpration(self):
        '''代操作预约测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'webAppointOpration')

    def test_webPickUpGoodsOpration(self):
        '''代操作提货测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'webPickUpGoodsOpration')

    def test_webHouseCallOpration(self):
        '''代操作上门测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'webHouseCallOpration')

    def test_webSignOpration(self):
        '''代操作签收测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'webSignOpration')

    def test_confirmCostOpration(self):
        '''大区成本提交测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'confirmCostOpration')

    def test_clearingCostOpration(self):
        '''大区结算测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'clearingCostOpration')

    def test_payCostOpration(self):
        '''大区支付测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'payCostOpration')

    def test_addFeeAuditOpration(self):
        '''增值审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'addFeeAuditOpration')

    def test_verifiyChangeOpration(self):
        '''核销变更测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'verifiyChangeOpration')


if __name__ == "__main__":
    unittest.main()



