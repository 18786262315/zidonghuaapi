# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class testSystemSortingOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/system_sorting_operation.xls'

    def test_qualitySortingOperation(self):
        '''质保分拣测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'qualitySortingOperation')

    def test_abnormalSortingOperation(self):
        '''异常分拣测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalSortingOperation')


if __name__ == "__main__":
    unittest.main()



