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
from API_1.common.do_mysql import Domysql
from API_1.common.get_data import GetData


congif = ReadConfig(path.conf_path)
log = Log()
test_data = Do_excel(path.case_path,'withdraw').read_data('WithdrawCase')

@ddt
class TestRegister(unittest.TestCase):

    def setUp(self):
        try:
            self.excel=Do_excel(path.case_path,'withdraw')
        except Exception as e :
            log.error('文件打开错误{}'.format(e))

    def tearDown(self):
        log.info('结束测试!')

    @data(*test_data)
    def test_succcess(self,case):

        global TestResult
        url = case['Url']
        method = case['Method']
        param = eval(regex(case['Param'])) #正则替换数据


        if case['Sql'] !=None:
            sql = eval(case['Sql'])['sql']
            before_amount = Domysql().do_mysql(sql)[0]
            log.info('提现之前的金额为{}'.format(before_amount))


        try:
            resp = HttpRequest().http_request(url,method,param,cookies=getattr(GetData,'COOKIES'))
            print(resp.json())
        except Exception as e :
            log.error('执行接口失败{}'.format(e))

        if resp.cookies:
            setattr(GetData,'COOKIES',resp.cookies)


        try:
            if case['Sql']!=None:
                sql =eval(case['Sql'])['sql']
                after_amount = Domysql().do_mysql(sql)[0]
                log.info('提现之后的金额为{}'.format(after_amount))

                draw_amount = int(param['amount'])
                log.info('提现金额{}'.format(draw_amount))
                except_amount = before_amount - draw_amount
                print('实际金额{}'.format(except_amount))
                self.assertEqual(except_amount,after_amount)

            if case['ExpectedResult'].find('money') !=-1:
                case['ExpectedResult'] = case['ExpectedResult'].replace('money',str(except_amount))


            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult = 'Pass'
        except Exception as e :
            log.error('执行接口测试出错,错误是{}'.format(e))
            TestResult = 'Fail'
            raise e

        finally:
            self.excel.wirte_back(case['CaseId']+1,9,resp.text)
            self.excel.wirte_back(case['CaseId']+1,10,TestResult)









