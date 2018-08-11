# -*- coding: utf8 -*-
# import sys
# import importlib
# importlib.reload(sys)
import os

import time
# sys.path.append('./AthenaTest')

import unittest
from HTMLTestRunner import HTMLTestRunner

os.chdir('./testcase/search_testcase')  # 将当前目录切换到 testcase/search_testcase 目录
# 指定测试用例为当前文件夹下的 testcase/search_testcase 目录
# test_dir = './testcase/search_testcase'
discover = unittest.defaultTestLoader.discover('./',pattern = 'test*.py')

if __name__ == "__main__":
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = '../../report/' + now + 'search_result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
							title='泛家居供应链管理系统查询接口测试报告')
	runner.run(discover)
	fp.close()