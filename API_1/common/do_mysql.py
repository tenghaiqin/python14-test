#-*- coding: utf-8 -*-
# @Time    : 2019/6/27 10:45
# @Author  : lemon_shan
# @Email   :1529755032@qq.com
# @File    : do_mysql.py

from mysql import connector
from API_1.common import path
from API_1.common.read_config import ReadConfig

config = ReadConfig(path.conf_path)

class Domysql:

    def  do_mysql(self,query,flag=1):

        db_config = config.get_data('DB','db_config')

        conn = connector.connect(**db_config)

        cursor = conn.cursor()

        cursor.execute(query)

        if flag ==1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        return res

if __name__ == '__main__':
    query = 'select max(Id) from loan where MemberID=88429'
    res = Domysql().do_mysql(query)
    print(res)

