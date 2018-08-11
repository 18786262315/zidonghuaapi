# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testWebQualityAssuranceOpration(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_quality_assurance_operation.xls'

    def test_qualityStartOperation(self):
        '''质保发起测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityStartOperation')

    def test_qualityHandOperation(self):
        '''质保处理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityHandOperation')

    def test_qualityTurnOperation(self):
        '''质保转派测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTrachOperation')

    def test_qualityTrachOpration(self):
        '''质保追踪测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTrachOperation')

    def test_qualityProcessManageOperation(self):
        '''质保流程管理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityProcessManageOperation')

    def test_qualityTerminateApplyOperation(self):
        '''质保流程终止申请测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTerminateApplyOperation')

    def test_qualityTerminateAuditOperation(self):
        '''质保流程终止审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualityTerminateAuditOperation')



if __name__ == "__main__":
    unittest.main()



