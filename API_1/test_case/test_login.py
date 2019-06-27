#-*- coding: utf-8 -*-
# @Time    : 2019/6/26 20:34
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : test_register.py

import unittest
from API_1.common import path
from API_1.common.http_request import HttpRequest
from API_1.common.read_config import ReadConfig
from API_1.common.regex import regex
from API_1.common.do_excel import Do_excel
from API_1.common.log import Log
from ddt import ddt,data

congif = ReadConfig(path.conf_path)
log = Log()
test_data = Do_excel(path.case_path,'login').read_data('LoginCase')

@ddt
class TestRegister(unittest.TestCase):

    def setUp(self):
        try:
            self.excel=Do_excel(path.case_path,'login')
        except Exception as e :
            log.error('文件打开错误{}'.format(e))

    def tearDown(self):
        log.info('结束测试!')

    @data(*test_data)
    def test_succcess(self,case):
        url = case['Url']
        method = case['Method']
        param = eval(regex(case['Param'])) #正则替换数据

        resp = HttpRequest().http_request(url,method,param)

        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult = 'Pass'
        except Exception as e :
            log.error('执行接口测试出错,错误是{}'.format(e))
            TestResult = 'Fail'
            raise e

        finally:
            self.excel.wirte_back(case['CaseId']+1,9,resp.text)
            self.excel.wirte_back(case['CaseId']+1,10,TestResult)









