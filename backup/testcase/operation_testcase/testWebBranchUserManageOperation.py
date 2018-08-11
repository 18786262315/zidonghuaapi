# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testWebBranchUserManageOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_branch_user_manage_operation.xls'

    def test_accountListOperation(self):
        '''账号列表测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'accountListOperation')

    def test_myAcountOperation(self):
        '''我的账号测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'myAcountOperation')




if __name__ == "__main__":
    unittest.main()



