#-*- coding: utf-8 -*-
#@time    : 2019/3/9 14:44
#@author  : lenmon_shan
#@Email   :1529755032@qq.com
#@file    : Request.py

# 1：根据提供的注册登录接口，完成注册登录接口的请求，至少每个接口有5条用例，每个接口要至少有一个正向用例。
#
# 2：要求如下：
# 1）http请求类（可以根据传递的method--get/post完成不同的请求），要求有返回值。
# 2）测试用例的数据存储在Excel中，并编写一个从Excel中读取数据的测试类，包含的函数能够读取测试数据，并且能够写回测试结果，要求有返回值。
# 3）新建一个run.py文件，在这里面完成Excel数据的读取以及完成用例的执行，并写回测试结果到Excel文档里面。 至此已经完成了接口自动化测试的第一步。
#


import requests


class HttpRequest:


    def http_request(self,url,param,method,cookies=None):
        '''rul:请求的url地址
        param:随接口发送的请求参数，以字典格式传递
        method:请求的方式  get post可以选择'''

        if method.upper()=='GET':#upper()函数来变成大写get
            print('正在发起get请求')

            try:
                resp=requests.get(url,params=param,cookies=cookies)
            except Exception as e:
                print('执行get请求报错，错误是{}'.format(e))
                resp='Error:get请求报错{}'.format(e)

        elif method.upper()=='POST':#upper()变成大写post
            print('正在发起post请求')

            try:
                resp=requests.post(url,data=param,cookies=cookies)
            except Exception as e:
                print('执行post请求报错，错误是{}'.format(e))
                resp = 'Error:get请求报错{}'.format(e)

        else:
            print('你的请求方式对！')
            resp='Error请求方法不对报错{}'.format(method)

        return resp#返回结果

if __name__ == '__main__':

    #测试注册接口是否正常
    # url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    # param = {'mobilephone': '15382876192', 'pwd': '123456', 'regname': 'lemonshanshan'}


    #测试登录接口是否正常
    url1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    param = {'mobilephone': '15382876192', 'pwd': '123456'}
    method = 'GET'
    res1 = HttpRequest().http_request(url1, param, method)

    # #充值接口
    # url2 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    # param1 = {'mobilephone': '15382876192', 'amount':'100.1'}
    # method = 'GET'
    # res2=HttpRequest().http_request(url2,param,method,cookies=res1.cookies)
    # print(res2.json())




    # # 竞标
    # url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/bidLoan'
    # param = {'memberId':'1123213','password':'123456','loanId':'','amount':'6000'}
    # method = 'GET'
    # res_1=HttpRequest().http_request(url_1,param,method)
    # print(res_1.json())
    #



