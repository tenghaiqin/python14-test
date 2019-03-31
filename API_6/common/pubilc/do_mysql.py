# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 20:03
# @Author  : lemon_shan
# @Email   : 1529755032@qq.com
# @File    : learn_mysql.py

from mysql import connector
from API_6.common.pubilc.read_config import ReadConfig
from API_6.common.pubilc import project_path
class DoMysql:
    '''操作数据库的类，专门进行数据读取'''

    def do_mysql(self,query,flag=1):
        '''
        :query sql查询语句
        :flag 标志 1 获取一条数据 2获取多条数据'''
        db_config=ReadConfig(project_path.conf_path).get_data('DB','db_config')#提示连接数据库信息

        cnn=connector.connect(**db_config)#建立一个链接
        cursor=cnn.cursor()#获取游标

        cursor.execute(query)#操作数据库

        if flag==1:
            res=cursor.fetchone()#返回的元组类型结果
        else:
            res=cursor.fetchall()#返回的是列表嵌套元组类型的结果

        return res
if __name__ == '__main__':
    query='select max(Id) from loan where MemberID=1123213'
    res=DoMysql().do_mysql(query,1)
    print('数据库的查询结果1：{}'.format(res))
