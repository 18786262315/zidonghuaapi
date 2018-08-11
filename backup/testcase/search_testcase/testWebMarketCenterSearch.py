# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebMarketCenterSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_market_center_search.xls'

    def test_cycleMerchantBillSearch(self):
        '''商家账单生成（逐单）'''
        datafile = self.datafile
        loadDatas(self, datafile, u'cycleMerchantBillSearch')

    def test_cycleMerchantBillStateSearch(self):
        '''逐单商家账单生成情况'''
        datafile = self.datafile
        loadDatas(self, datafile, u'cycleMerchantBillStateSearch')

    def test_singleMerchantBillSearch(self):
        '''商家账单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'singleMerchantBillSearch')

    def test_merchantBillAuditSearch(self):
        '''商家账单审核'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantBillAuditSearch')


        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")



if __name__ == "__main__":
    unittest.main()



