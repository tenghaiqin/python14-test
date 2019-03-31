#-*- coding: utf-8 -*-
#@time    : 2019/3/17 8:25
#@author  : lenmon_shan
#@Email   :1529755032@qq.com
#@file    : login.py

import unittest  #导入unittest模块
from API_3.common.pubilc.http_request import HttpRequest#导入Http请求
from API_3.common.pubilc.do_excel import DoExcel#导入测试用例
from API_3.common.pubilc import project_path#导入路径全局变量
from ddt import ddt,data #导入DDT
from API_3.common.pubilc.my_log import MyLog#导入日志
from openpyxl import load_workbook
import requests

test_session = requests.session()
class login:
    def __init__(self):

        '''获取cookies '''
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        param = {'mobilephone': '15382876192', 'pwd': '123456'}
        resp = test_session.post(url, data=param)
        # cookies = resp.cookies
        # print(cookies)

    def http_request(self,rul,param,method):#定义默认值使用get方式
        '''rul:请求的url地址
        param:随接口发送的请求参数，以字典格式传递
        method:请求的方式  get post可以选择'''

        if method.upper()=='GET':#变成小写get
            print('正在发起get请求')

            try:
                resp=test_session.get(rul,params=param)
            except Exception as e:
                print('执行get请求报错，错误是{}'.format(e))
                resp='Error:get请求报错{}'.format(e)

        elif method.upper()=='POST':
            print('正在发起post请求')

            try:
                resp=test_session.post(rul,data=param)
            except Exception as e:
                print('执行post请求报错，错误是{}'.format(e))
                resp = 'Error:get请求报错{}'.format(e)

        else:
            print('你的请求方式对！')
            resp='Error请求方法不对报错{}'.format(method)

        return resp.json()#返回结果
#


    # def recharge(self,url_1,param):
    #
    #     resp = test_session.post(url_1, data=param)
    #     resp = test_session.post(url_1, param)
    #     print(resp.json())

# test_session = requests.session()
url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
param = {'mobilephone': '15382876192', 'amount': '10000'}
method='GET'
# login().recharge(url_1, param)
res_1=login().http_request(url_1,param,method)
print(res_1)



# if __name__ == '__main__':
#     test_session = requests.session()
#     url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
#     param = {'mobilephone': '15382876192', 'amount': '10000'}
#     method='POST'
#     res_1=HttpRequest(test_session).http_request(url_1,param,method)
#     print(res_1.json())
