# -*- coding: utf-8 -*-
# @Time      :2019-03-07 11:55
# @Author    :lenmon_shan
# @Email     :1529755032@qq.com
# @File      :class_unittest.py
# @Software :PyCharm

import unittest  #导入unittest模块
from API_6.common.pubilc.http_request import HttpRequest#导入Http请求
from API_6.common.pubilc.do_excel import DoExcel#导入测试用例
from API_6.common.pubilc import project_path#导入路径全局变量
from ddt import ddt,data #导入DDT
from API_6.common.pubilc.my_log import MyLog#导入日志
from API_6.common.pubilc.do_mysql import DoMysql
from API_6.common.pubilc.get_data import GetData
from API_6.common.pubilc import do_regex

my_log = MyLog()#存储log位置的变量
#获取add_loan模块的测试数据
test_data=DoExcel(project_path.case_path,'add_loan').read_data('AddLoanCase')

@ddt#装饰测试类
class TestHttpRequest(unittest.TestCase):#继承

    def setUp(self):
        '''写入测试结果的对象'''
        try:
            self.t=DoExcel(project_path.case_path,'add_loan')
        except Exception as e:
            my_log.error('文件打开出错了{}'.format(e))#调用log类

    @data(*test_data)#装饰测试用例
    def test_case_001(self,case):
        # 开始发起测试
        method = case['Method']
        url = case['Url']

        #替换mobilePhone,pwd,loanid
        param=eval(do_regex.replace(case['Param']))

        my_log.info('**************************************')#日志记录
        my_log.info('正在执行{}模块的第{}条用例:{}'.format(case['Module'],case['CaseId'],case['Title']))#日志记录
        my_log.info('请求的测试数据是{}'.format(case))#日志记录
        resp=HttpRequest().http_request(url,param,method,cookies=getattr(GetData,'COOKIES'))
        print(resp.json())

         #发送请求前后判断是否要查询数据库的loan_Id
        if case['Sql']!=None:
            loan_Id=DoMysql().do_mysql(eval(case['Sql'])['sql'],1)# 原来是字符串，eval转换为字典格式
            setattr(GetData,'loanid',str(loan_Id[0]))#利用反射 这里面的loanid要与xlsx文件保持一致，loan_Id获取到的是int类型，使用str转成字符串
            #setattr是动态的，不管Getdata有没有这个属性值，都可以使用

         #发生请求后再加一个判断，是否产生cookies
        if resp.cookies:
            setattr(GetData,'COOKIES',resp.cookies)
      # 断言：判断期望结果和实际结果是否一致
        try:
            self.assertEqual(eval(case['ExpectedResult']),resp.json())
            TestResult='Pass'#如果一致，测试结果为PASS
        except AssertionError as e:#否则报错并打fail
            my_log.error('执行接口测试出错，错误是{}'.format(e))#日志记录
            TestResult = 'Fail'
            raise e
        finally:#执行完毕后，最终都要写入结果到Excel中
            my_log.info('**********开始写入数据***********')#日志记录
            self.t.write_back(case['CaseId']+1,9,str(resp.json()))#写入实际结果
            self.t.write_back(case['CaseId']+1,10,TestResult)
            my_log.info('**********写入数据完毕***********')#日志记录
        my_log.info('第{}条测试用例执行结果是{}'.format(case['CaseId'], resp.json()))#日志记录
        my_log.info('该条用例的测试结论是{}'.format(TestResult))#日志记录

    #结束测试
    def tearDown(self):
        print('已结束测试啦！')

