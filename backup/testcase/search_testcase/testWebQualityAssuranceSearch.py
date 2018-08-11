# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebQualityAssuranceSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_quality_assurance_search.xls'

    def test_qualityStartSearch(self):
        '''质保发起列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityStartSearch')

    def test_qualityHandSearch(self):
        '''质保处理列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityHandSearch')

    def test_qualityTurnSearch(self):
        '''质保转派列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTurnSearch')

    def test_qualitySubOrderSearch(self):
        '''质保衍生单列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualitySubOrderSearch')

    def test_qualityTrachSearch(self):
        '''质保追踪列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTrachSearch')

    def test_qualityProcessManageSearch(self):
        '''质保流程管理列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityProcessManageSearch')

    def test_qualityTerminateApplySearch(self):
        '''质保流程终止申请列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTerminateApplySearch')

    def test_qualityTerminateAuditSearch(self):
        '''质保流程终止审核列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTerminateAuditSearch')

if __name__ == "__main__":
    unittest.main()
