# -*- coding: utf-8 -*- 
# @Time : 2020/12/28 20:37 
# @Author : dujun
# @describe : 数据库封装
# @File : dataBase.py

import pymysql
import pytest


class DataBase:
    def __init__(self):
        # 测试环境
        host = '192.168.18.203'
        port = 3307
        user = 'root'
        password = 'testtest '
        database = 'user'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password,database=database)
        self.cursor = self.conn.cursor()

    # select
    def select(self):
        try:
            sql1 = "SELECT * FROM `us_user_users` WHERE   ShenFenZH  LIKE '%haitun_';"
            self.cursor.execute(sql1)
            self.conn.commit()
            sql1_value = self.cursor.fetchmany(2)
            print(sql1_value[0])

        except BaseException:
            self.conn.rollback()


if __name__ == '__main__':
    run = DataBase()
    run.select()
