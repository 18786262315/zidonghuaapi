# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebSystemSortingSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_system_sorting_search.xls'

    def test_qualitySortingSearch(self):
        '''质保分拣列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualitySortingSearch')

    def test_abnormalSortingSearch(self):
        '''VIP发起列表查询'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalSortingSearch')

if __name__ == "__main__":
    unittest.main()
