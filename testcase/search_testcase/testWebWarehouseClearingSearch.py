# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebWarehouseClearingSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_warehouse_clearing_search.xls'

    def test_cycleTrunkBillSearch(self):
        '''物流账单（按点）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'cycleTrunkBillSearch')

    def test_noncycleTrunkBillSearch(self):
        '''物流账单（自营）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'noncycleTrunkBillSearch')

    def test_trunkBillAuditSearch(self):
        '''物流账单审核'''
        datafile = self.datafile
        loadDatas(self, datafile, u'trunkBillAuditSearch')


            # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")

if __name__ == "__main__":
    unittest.main()



