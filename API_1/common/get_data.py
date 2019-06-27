#-*- coding: utf-8 -*-
# @Time    : 2019/6/27 9:53
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : get_data.py

from API_1.common.read_config import ReadConfig
from API_1.common import path

config = ReadConfig(path.conf_path)


class GetData:
    test = None
    COOKIES =None
    loanid =None
    phone = config.get_str('MobilePhone','phone')
    pwd = config.get_str('MobilePhone','pwd')
    member_id = config.get_str('MobilePhone','member_id')


if __name__ == '__main__':
    print(GetData.test)
    print(getattr(GetData,'test'))
    print(hasattr(GetData,'test'))
    print(setattr(GetData,'test','123456'))
    a = (getattr(GetData,'test'))
    print(a)








