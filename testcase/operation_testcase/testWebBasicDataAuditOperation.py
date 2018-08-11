# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testWebBasicDataAuditOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/web_basic_data_audit_operation.xls'

    def test_branchInfoAuditOperation(self):
        '''网点基础资料审核测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'branchInfoAuditOperation')



if __name__ == "__main__":
    unittest.main()



