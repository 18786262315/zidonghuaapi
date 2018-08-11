# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testWebQualityAssuranceOpration(unittest.TestCase):

    def setUp(self):
        self.datafile = 'E:\AutoTest\InterfaceTest\AthenaTest\datacase\opration_datacase\web_quality_assurance_opration.xls'

    def test_qualityStartOpration(self):
        '''质保发起测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityStartOpration')

    def test_qualityHandOpration(self):
        '''质保处理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityHandOpration')

    def test_qualityTurnOpration(self):
        '''质保转派测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTurnOpration')

    def test_qualityTrachOpration(self):
        '''质保追踪测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTrachOpration')

    def test_qualityProcessManageOpration(self):
        '''质保流程管理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityProcessManageOpration')

    def test_qualityTerminateApplyOpration(self):
        '''质保流程终止申请测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTerminateApplyOpration')

    def test_qualityTerminateAuditOpration(self):
        '''质保流程终止审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTerminateAuditOpration')



if __name__ == "__main__":
    unittest.main()



