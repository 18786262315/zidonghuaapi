# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebCreditManageSearch(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/search_datacase/web_credit_manage_search.xls'

    def test_merchantCridetSearch(self):
        '''商家授信'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantCridetSearch')


if __name__ == "__main__":
    unittest.main()


