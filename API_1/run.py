#-*- coding: utf-8 -*-
# @Time    : 2019/6/26 23:22
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : run.py

import sys
sys.path.append('./')

import unittest
import HTMLTestRunnerNew
from API_1.test_case import test_register
from API_1.test_case import test_draw
from API_1.test_case import test_login
from API_1.test_case import test_recharge
from API_1.test_case import test_addLoan
from API_1.common import path

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_draw))
suite.addTest(loader.loadTestsFromModule(test_login))
suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_addLoan))

with open(path.report_path,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='python',
                                              description='这是备注',
                                              tester='shanshan')

    runner.run(suite)

