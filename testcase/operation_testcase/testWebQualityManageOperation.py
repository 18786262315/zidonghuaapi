# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebQualityManageOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_quality_manage_operation.xls'

    def test_kpiTrunkOpration(self):
        '''KPI物流考核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'kpiTrunkOpration')

    def test_kpiBranchOpration(self):
        '''KPI网点考核审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'kpiBranchOpration')

    def test_complainInfoOpration(self):
        '''奖罚单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'complainInfoOpration')

    def test_complainHandleOprtion(self):
        '''申诉处理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'complainHandleOprtion')

if __name__ == "__main__":
    unittest.main()