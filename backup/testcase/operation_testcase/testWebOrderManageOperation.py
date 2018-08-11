# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebOrderManageOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_order_manage_operation.xls'

    def test_addData(self):
        '''录单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'addData')

    def test_importOrderOpration(self):
        '''暂存单导单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'importOrderOpration')

    def test_codeCreateOpration(self):
        '''预生单号生成测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'codeCreateOpration')

    def test_preparationImportOpration(self):
        '''预生单导入测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'preparationImportOpration')

    def test_addTempOrderOpration(self):
        '''暂存单提交测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'addTempOrderOpration')

    def test_importTurnRegularOpration(self):
        '''暂存单直接转正测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'importTurnRegularOpration')

    def test_addOrderFollowOpration(self):
        '''订单查询-跟进提交测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'addOrderFollowOpration')

    def test_deleteOrderOpration(self):
        '''导单删除测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'deleteOrderOpration')

    def test_msExcelOpration(self):
        '''暂存单匹配测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'msExcelOpration')

    def test_jdOrderCancelOpration(self):
        '''京东订单取消测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'jdOrderCancelOpration')

    def test_orderExceptionOpration(self):
        '''补件单转正测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderExceptionOpration')

    def test_subOrderOpration(self):
        '''衍生单查询详情测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'subOrderOpration')


if __name__ == "__main__":
    unittest.main()



