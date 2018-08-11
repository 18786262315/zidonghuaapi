# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebOrderManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_order_manage_search.xls'

    def test_importDirectSearch(self):
        '''直营导单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'importDirectSearch')

    def test_addOrderSearch(self):
        '''录单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'addOrderSearch')

    def test_importOrderSearch(self):
        '''暂存单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'importOrderSearch')

    def test_TMSOrderSearch(self):
        '''TMS绑单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'TMSOrderSearch')

    def test_printOrderSearch(self):
        '''打印订单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'printOrderSearch')

    def test_allOrderSearch(self):
        '''订单查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'allOrderSearch')

    def test_deleteOrderSearch(self):
        '''导单删除列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'deleteOrderSearch')

    def test_msExcelSearch(self):
        '''暂存单匹配列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'msExcelSearch')

    def test_jdOrderCancelSearch(self):
        '''京东推单取消列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'jdOrderCancelSearch')

    def test_orderExceptionSearch(self):
        '''补件单列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'orderExceptionSearch')

    def test_subOrderSearch(self):
        '''衍生单查询列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'subOrderSearch')

if __name__ == "__main__":
    unittest.main()



