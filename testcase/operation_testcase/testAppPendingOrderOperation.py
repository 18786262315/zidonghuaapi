# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppPendingOrderOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/app_pending_order_operation.xls'

    def test_appPickUpGoodsOpration(self):
        '''app提货测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appPickUpGoodsOpration')

    def test_appHouseCallOprationOpration(self):
        '''app上门测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appHouseCallOprationOpration')

    def test_appSignOpration(self):
        '''app签收测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appSignOpration')

    def test_changeOrderAppointOpration(self):
        '''app修改预约测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'changeOrderAppointOpration')

    def test_appAddFeeOpration(self):
        '''app发起增值费测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appAddFeeOpration')

    def test_appOrderTurnOpration(self):
        '''app转单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appOrderTurnOpration')

    def test_abnormaStartOpration(self):
        '''app发起异常测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormaStartOpration')

if __name__ == "__main__":
    unittest.main()