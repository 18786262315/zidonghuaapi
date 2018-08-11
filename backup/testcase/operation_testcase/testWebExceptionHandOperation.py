# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebExceptionHandOpration(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_exception_hand_operation.xls'

    def test_trunkAbnormalOpration(self):
        '''干线自提异常测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkAbnormalOpration')

    def test_VIPAbnormalOpration(self):
        '''VIP发起测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'VIPAbnormalOpration')

    def test_abnormalTrackOpration(self):
        '''异常追踪测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTrackOpration')

    def test_abnormalTurnOpration(self):
        '''异常转派测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTurnOpration')

    def test_abnormalTodoOpration(self):
        '''异常待办测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTodoOpration')

    def test_adnormalProcessManageOpration(self):
        '''异常流程管理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'adnormalProcessManageOpration')

    def test_abnormalTerminateApplyOpration(self):
        '''异常流程终止申请测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTerminateApplyOpration')

    def test_abnormalTerminateAuditOpration(self):
        '''异常流程终止审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTerminateAuditOpration')



if __name__ == "__main__":
    unittest.main()



