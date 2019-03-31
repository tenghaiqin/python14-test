#-*- coding: utf-8 -*-
#@time    : 2019/3/28 10:32
#@author  : lenmon_shan
#@Email   :1529755032@qq.com
#@file    : do_regex.py

import re
from API_6.common.pubilc.get_data import GetData

def replace(target):#target:目标
    p='#(.*?)#'#元字符
    while re.search(p,target): #查询参数的字符串math 为True
        m=re.search(p,target)
        key=m.group(1)#传参数1 表示只传一组
        print('key:',key)
        value=getattr(GetData,key)#通过GetData获取值
        target=re.sub(p,value,target,count=1)#count=1这里是替换一次
    return target

if __name__ == '__main__':
    target ="{'mobile_phone':'#phone#','pwd':'#pwd#','memberId':'#member_id#'}"
    m=replace(target)
    print(m)















