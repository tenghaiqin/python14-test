#-*- coding: utf-8 -*-
# @Time    : 2019/6/26 17:47
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : http_request.py

import requests

class HttpRequest:

    def http_request(self,url,method,param,cookies=None):
        if method.upper()=='GET':
            try:
                res=requests.get(url,param,cookies=cookies)
            except Exception as e:
                res = 'ERROR执行get请求出错{}'.format(e)
        elif method.upper()=='POST':
            try:
                res=requests.post(url,param,cookies=cookies)
            except Exception as e:
                res = 'ERROR执行past请求出错{}'.format(e)
        else:
            print('请求方式不正确')
            res='ERRRO请求方法不正确{}'.format(method)

        return res


if __name__ == '__main__':
    log_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    list_url = 'http://test.lemonban.com/futureloan/mvc/api/member/list/member/list'
    loan_url = 'http://test.lemonban.com/futureloan/mvc/api/loan/getLoanList'
    param = {'mobilephone': '15382876192', 'pwd': '123456', '注册名': 'shanshan'}
    method='GET'

    login_res = HttpRequest().http_request(log_url,method,param=param)
    print(login_res)
    print(login_res.json())

    # list_res = HttpRequest().http_request(list_url, method, param=None)
    # list_res = HttpRequest().http_request(list_url,method,param=None,cookies=login_res.cookies)
    # print(list_res)
    # print(list_res.json())

    # loanlist_res = HttpRequest().http_request(loan_url, method, param=None)
    loanlist_res = HttpRequest().http_request(loan_url,method,param=None,cookies=login_res.cookies)
    print(loanlist_res)
    print(loanlist_res.json())


