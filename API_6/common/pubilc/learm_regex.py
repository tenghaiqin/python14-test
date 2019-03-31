#-*- coding: utf-8 -*-
#@time    : 2019/3/26 22:30
#@author  : lenmon_shan
#@Email   :1529755032@qq.com
#@file    : learm_regex.py


#正则表达式

# 正则表达式是对字符串（包括普通字符（例如，a 到 z 之间的字母）和特殊字符（称为“元字符”））操作的一种逻辑公式，编写一些规范来查找需要的字符串
#正则表达式的组成：原义字符和元字符  2种
#（）表示一个组，通俗的理解就是用它来标记一个表示式组的开始和结束

#元字符：
#  . :可以匹配任意单个字符，汉字，字母，符号，数字
# \d :可以匹配任意单个数字

#限定符：
#  + : 至少匹配一次
#  ? :多最匹配一次
#  * :匹配0次或者多次

#场景：
#参数化
#查找一些特殊的字符：邮箱，手机格式 ，身份证号码

import re
from API_6.common.pubilc.get_data import GetData


#re.search() 对字符中任意位置进行,匹配到一个就返回，后面就不会再匹配
#re.match()    从字符中开头位置开始匹配
#re.findall()  查找所有匹配的字符，返回是一个列表
#re.finditer()
#.group()返回已找到的原义字符
#re.usb()替换


# #原义字符的查找
# a ="{'mobile_phone':'phone','pwd':'pwd'}"
# p='phone'#原义字符的查找
# res1=re.search(p,a) #在目标字符串里面根据正则表达来查询字符串，有就返回对象，没有就返回None
# print(res1)
# print('原义字符的查找:',res1.group())
#
# #元字符的查找多次 .*
# a ="{'mobile_phone':'#phone#','pwd':'#pwd#'}"
# p2='#(.*)#'  #()是正则表达式里面表示一个组，##是表达式，
# res2=re.search(p2,a)
# print(res2)
# print('元字符的查找多次:',res2.group())
#
# #元字符的查找 ,最多匹配一次，#加上一个?
# a ="{'mobile_phone':'#phone#','pwd':'#pwd#'}"
# p3='#(.*?)#'
# res3=re.search(p3,a)
# print(res3)
# print('元字符的查找，最多匹配一次:',res3.group())#不传参，返回的是表达式##和字符串一起
#
# #元字符的查找 ,最多匹配一次，找到里面的key
# a ="{'mobile_phone':'#phone#','pwd':'#pwd#'}"
# p3='#(.*?)#'
# res3=re.search(p3,a)
# print(res3)
# print('元字符的查找，最多匹配一次，找到里面的key:',res3.group(1))#传参，加上索引位置1，只返回匹配的字符串
# res4=re.findall(p3,a)#查找所有匹配的字符，返回是一个列表
# print('查找所有匹配的字符:',res4)
#
# #替换Key值,#一种方法,直接输入数字
# a2=re.sub(p3,'15382876192',a,count=1)
# print('a2替换后的值是:',a2)
#
# #替换Key值,2种方法,从配置文件获取数据
# from API_5.common.pubilc import project_path
# from API_5.common.pubilc.read_config import ReadConfig
#
# a4 ="{'mobile_phone':'#phone#','pwd':'#pwd#'}"
# p4='#(.*?)#'
#
# phone=ReadConfig(project_path.conf_path).get_str('MobilePhone','phone')#从配置文件读取key值
# a3=re.sub(p4,phone,a4,count=1) #
# print('a3替换后的值是:',a3)
#
#
# a5 ="{'mobile_phone':'#phone#','pwd':'#pwd#'}"
# p5='#(.*?)#'
# res5=re.search(p5,a5) #在目标字符串里面根据正则表达来查询字符串，有就返回对象
# print('res5:',res5.group(1))#传参，加上索引位置1，只返回匹配的字符串
# print('res5:',re.findall(p5,a5))#查找所有匹配的字符，返回是一个列表

#使用while循环进行正则表示工的替换值

a ="{'mobile_phone':'#phone#','pwd':'#pwd#'}"
p2='#(.*?)#'

while re.search(p2,a):
    m=re.search(p2,a) #在目标字符串里面根据正则表达来查询字符串，有就返回对象
    key=m.group(1)#传参，加上索引位置1，只返回匹配的字符串
    print('key:',key)
    value=getattr(GetData,key)#替换值
    a=re.sub(p2,value,a,count=1)#把value值替换之后再重新赋值给a
print(a)



