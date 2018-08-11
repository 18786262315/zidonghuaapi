# -*- coding: utf8 -*-
import unittest
from AthenaTest.common.loadDatas import *

import sys
import importlib
importlib.reload(sys)

class TestAppAppointDistributionOperation(unittest.TestCase):

    def setUp(self):
        self.datafile = '../../datacase/operation_datacase/app_appoint_distribution_operation.xls'

    def test_appOrderAppointOpration(self):
        '''app预约、派单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appOrderAppointOpration')

    def test_appOrderDistributionOpration(self):
        '''单个、多单派单测试'''
        datafile = self.datafile
        loadDatas(self, datafile, u'appOrderDistributionOpration')

if __name__ == "__main__":
    unittest.main()