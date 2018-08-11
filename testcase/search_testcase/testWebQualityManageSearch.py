# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebQualityManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_quality_manage_search.xls'

    def test_kpiTrunkSearch(self):
        '''KPI物流考核'''
        datafile = self.datafile
        loadDatas(self, datafile, u'kpiTrunkSearch')

    def test_kpiBranchSearch(self):
        '''KPI网点考核'''
        datafile = self.datafile
        loadDatas(self, datafile, u'kpiBranchSearch')

    def test_complainInfoSearch(self):
        '''奖惩单'''
        datafile = self.datafile
        loadDatas(self, datafile, u'complainInfoSearch')

    def test_complainHandleSearch(self):
        '''申诉处理'''
        datafile = self.datafile
        loadDatas(self, datafile, u'complainHandleSearch')






        # 这块移动到loadDatas中进行处理
        #errortest = loadDatas(self, datafile, u'addData')
        #print(errortest)
        #for result in errortest:
            #with self.subTest(data=result):  # 注意subTest的用法
                #self.assertEqual(result, "pass")


if __name__ == "__main__":
    unittest.main()



