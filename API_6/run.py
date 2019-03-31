#-*- coding: utf-8 -*-
#@time    : 2019/3/13 23:39
#@author  : lenmon_shan
#@Email   :1529755032@qq.com
#@file    : run.py


import sys
# sys.path.append('引用模块的地址')
# 该路径已经添加到系统的环境变量了，当我们要添加自己的搜索目录时，可以通过列表的append()方法；
# 对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append(‘xxx’)：
sys.path.append('./')#添加上一级目录
print(sys.path)


import unittest
import HTMLTestRunnerNew
from API_6.common.pubilc import project_path
from API_6.test_case import test_login
from API_6.test_case import test_recharge
from API_6.test_case import test_withdraw
from API_6.test_case import test_add_loan
from API_6.test_case import test_invest



#新建一个测试集
suite=unittest.TestSuite()

# 添加用例
loader=unittest.TestLoader()#加载测试用例
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest)) #添加测试用例具体到方法
suite.addTest(loader.loadTestsFromModule(test_login))#添加充值用例 具体到模块
# suite.addTest(loader.loadTestsFromModule(test_recharge))#添加充值用例 具体到模块


#执行用例 生成测试报告
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='py0330测试报告',
                                            description='14的测试报告',
                                            tester='shanshan')
    runner.run(suite)#执行用例  传入suite suite里面是我们收集的测试用例
