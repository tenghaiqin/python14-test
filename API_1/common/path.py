#-*- coding: utf-8 -*-
# @Time    : 2019/6/26 18:09
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : path.py


import sys
import os

path = os.path.realpath(__file__)
# print(path)

common_path = os.path.split(path)[0]
# print(common_path)

api_path = os.path.split(common_path)[0]
# print(api_path)

case_path = os.path.join(api_path,'data','test_api.xlsx')
# print(case_path)

conf_path = os.path.join(api_path,'conf','test.conf')
# print(conf_path)

log_path = os.path.join(api_path,'log','test.log')

report_path = os.path.join(api_path,'report','test.html')