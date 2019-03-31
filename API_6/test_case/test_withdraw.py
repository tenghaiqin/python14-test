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
from API_6.common.pubilc import do_regex
from API_6.common.pubilc.do_mysql import DoMysql

my_log = MyLog()#存储log位置的变量
COOKIES=None#设置cookies的初始值为None 第一种方法来设置cookies

#获取测试数据--测试提现
test_data=DoExcel(project_path.case_path,'withdraw').read_data('WithdrawCase')


@ddt#装饰测试类
class TestHttpRequest(unittest.TestCase):#继承

    def setUp(self):
        '''创建写入的测试实例'''

        try:
            self.t=DoExcel(project_path.case_path,'withdraw')#写入测试结果的对象
        except Exception as e:
            print('文件打开出错了{}'.format(e))
            my_log.error(e)#调用log类

    # 写用例
    @data(*test_data)#装饰测试用例
    def test_cases(self,case):

        global COOKIES #声明这是一个全局变量
        # 开始发起测试
        method = case['Method']
        url = case['Url']

        # 正则表达式替换mobilePhone,pwd
        param = eval(do_regex.replace(case['Param'])) # 原来是字符串，eval转换为字典格式

        my_log.info('**************************************')#日志记录
        my_log.info('正在执行{}模块的第{}条用例:{}'.format(case['Module'],case['CaseId'],case['Title']))#日志记录
        my_log.info('请求的测试数据是{}'.format(case))#日志记录

        #提现之前查询金额
        if case['Sql']!=None:
            before_amount=DoMysql().do_mysql(eval(case['Sql'])['sql'])[0]#获取到的sql是一个字符类型，所以要eval转成字典类型

        resp=HttpRequest().http_request(url,param,method,cookies=COOKIES)
        print('状态码:',resp)

        #加判断,如果产生cookies
        if resp.cookies:#判断请求的cookies是否为空 ，不为空就是True
            COOKIES=resp.cookies#更新全局变量的值

        try:
            # 发送请求后再查询提示之后的金额
            if case['Sql']!=None:
                after_amount = DoMysql().do_mysql(eval(case['Sql'])['sql'])[0]#查询提现之后的金额
                withdraw_amount=int(param['amount'])#提现金额是一个字符串，在int来转换一下
                except_amount=before_amount-withdraw_amount# 提现前金额-提现金额=提现后的金额
                print(type(except_amount))
                self.assertEqual(except_amount,after_amount)#断言，提现金额是否一致

             #判断是否替换期望值
            if  case['ExpectedResult'].find('money')!=-1:
                case['ExpectedResult']=case['ExpectedResult'].replace('money',str(except_amount))#完成预期结果的替换之后才能进行断言

            self.assertEqual(eval(case['ExpectedResult']), resp.json())  # 断言：判断期望结果和实际结果是否一致
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
