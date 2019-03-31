#-*- coding: utf-8 -*-
#@time    : 2019/3/19 22:11
#@author  : lenmon_shan
#@Email   :1529755032@qq.com
#@file    : get_data.py

from API_6.common.pubilc import project_path
from API_6.common.pubilc import read_config
config=read_config.ReadConfig(project_path.conf_path)

# 反射  getattr(类名，类属性名) 新知识

class GetData:
    '''用来获取动态数据的更改 删除 获取数据'''
    COOKIES=None
    LOAN_ID=None
    LEAVE_AMOUNT=None#投资金额
    RECHARGE_AMOUNT=None#充值金额
    phone=config.get_str('MobilePhone','phone')
    pwd=config.get_str('MobilePhone','pwd')
    member_id=config.get_str('MobilePhone','member_id')

if __name__ == '__main__':

    print(GetData.cookies)
    print(GetData().cookies)

    # getattr()#反射来取值
    print(getattr(GetData,'cookies'))#获取属性值
    print(hasattr(GetData,'cookies'))#判断是否有这个属性值存在，返回值是布尔值
    print(setattr(GetData,'cookies','123456'))#设置新值，返回是None.第一个是类名，第二个是属性名，第三个是要设置的属性值
    # print(delattr(GetData,'cookies'))#删除某个属性值 这个不常用

    print(getattr(GetData,'cookies'))
