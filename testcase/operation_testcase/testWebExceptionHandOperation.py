# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebExceptionHandOpration(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_exception_hand_operation.xls'

    def test_trunkAbnormalOperation(self):
        '''干线自提异常测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkAbnormalOperation')

    def test_VIPAbnormalOperation(self):
        '''VIP发起测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'VIPAbnormalOperation')

    def test_abnormalTrackOperation(self):
        '''异常追踪测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTrackOperation')

    def test_abnormalTurnOperation(self):
        '''异常转派测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTurnOperation')

    def test_abnormalTodoOperation(self):
        '''异常待办测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTodoOperation')

    def test_adnormalProcessManageOperation(self):
        '''异常流程管理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'adnormalProcessManageOperation')

    def test_abnormalTerminateApplyOperation(self):
        '''异常流程终止申请测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTerminateApplyOperation')

    def test_abnormalTerminateAuditOperation(self):
        '''异常流程终止审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTerminateAuditOperation')



if __name__ == "__main__":
    unittest.main()



