#-*- coding: utf-8 -*-
#@time    : 2019/3/12 8:49
#@author  : lenmon_shan
#@Email   :1529755032@qq.com
#@file    : project_path.py


import os

#文件的路径 放到这里  os.path.realpat
project_path=os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]#切割
# print(project_path)


#切割一次路径 os.path.split

#测试用例 存储的路径
case_path=os.path.join(project_path,'test_case','test_api.xlsx')
# print(case_path)

project_path_2=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]#切割

#配置文件的路径
conf_path=os.path.join(project_path_2,'conf','case.conf')
# print(conf_path)

#日志的路径
log_path=os.path.join(project_path,'result','test_log','test.log')
# print(log_path)

report_path=os.path.join(project_path,'result','test_report','test_report.html')
# print(report_path)