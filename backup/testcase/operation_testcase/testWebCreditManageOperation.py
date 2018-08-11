# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebCreditManageOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_credit_manage_operation.xls'

    def test_merchantCridetOpration(self):
        '''商家授信测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'merchantCridetOpration')


if __name__ == "__main__":
    unittest.main()