# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppMyexceptionHandOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/app_myexception_hand_operation.xls'

    def test_abnormalTodoOpration(self):
        '''我的发起-异常详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTodoOpration')

    def test_abnormalTrackOpration(self):
        '''我的待办-异常详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTrackOpration')

    def test_abnormalEndOpration(self):
        '''已完结-异常详情'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalEndOpration')

if __name__ == "__main__":
    unittest.main()