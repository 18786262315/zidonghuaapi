# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testWebWarehouseUserManageOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_warehouse_user_manage_operation.xls'

    def test_accountListOperation(self):
        '''账号列表测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'accountListOperation')

    def test_myAcountOperation(self):
        '''我的账号测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'myAcountOperation')

    def test_roleManageOperation(self):
        '''角色管理测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'roleManageOperation')




if __name__ == "__main__":
    unittest.main()



