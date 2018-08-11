# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppExceptionHandOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/app_exception_hand_operation.xls'

    def test_abnormalTodoOpration(self):
        '''异常待办测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTodoOpration')

    def test_abnormalTrackOpration(self):
        '''异常追踪详情测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalTrackOpration')

    def test_abnormalEndOpration(self):
        '''已完结异常详情测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'abnormalEndOpration')

if __name__ == "__main__":
    unittest.main()