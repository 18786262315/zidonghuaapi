# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestWebBranchViolateManageOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_branch_violate_manage_operation.xls'

    def test_branchViolateManageOpration(self):
        '''申诉处理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'branchViolateManageOpration')

if __name__ == "__main__":
    unittest.main()