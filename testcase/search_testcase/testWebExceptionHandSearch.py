# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebExceptionHandSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_exception_hand_search.xls'

    def test_trunkAbnormalSearch(self):
        '''干线自提异常列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkAbnormalSearch')

    def test_orderVIPAbnormalSearch(self):
        '''VIP发起列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'VIPAbnormalSearch')

    def test_abnormalTrackSearch(self):
        '''异常追踪列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTrackSearch')

    def test_abnormalTurnSearch(self):
        '''异常转派列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTurnSearch')

    def test_abnormalTodoSearch(self):
        '''异常待办列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTodoSearch')

    def test_adnormalProcessManageSearch(self):
        '''异常流程管理列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'adnormalProcessManageSearch')

    def test_abnormalTerminateApplySearch(self):
        '''异常流程终止申请列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTerminateApplySearch')

    def test_abnormalTerminateAuditSearch(self):
        '''异常流程终止审核列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTerminateAuditSearch')

if __name__ == "__main__":
    unittest.main()
