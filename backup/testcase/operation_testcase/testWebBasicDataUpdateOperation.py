# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testWebBasicDataUpdateOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_basic_data_update_operation.xls'

    def test_branchInfoUpdateOperation(self):
        '''网点基础资料维护测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'branchInfoUpdateOperation')



if __name__ == "__main__":
    unittest.main()



