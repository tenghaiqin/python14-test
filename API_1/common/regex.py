#-*- coding: utf-8 -*-
# @Time    : 2019/6/27 9:48
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : regex.py

import re
from API_1.common.get_data import GetData

def regex(t):
    p= '#(.*?)#'
    while re.search(p,t):
        m = re.search(p,t)
        key = m.group(1)
        print('key:',key)
        value = getattr(GetData,key)
        print('value:',value)
        t = re.sub(p,value,t,count=1)
    return t

if __name__ == '__main__':
    t = "{'mobile_phone':'#phone#','pwd':'#pwd#','memberId':'#member_id#'}"
    m = regex(t)
    print(m)

