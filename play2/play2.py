#  -*- coding:utf-8 -*-

# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

__author__ = 'jqbk'
__date__ = '2017-06-20'

import os
import sys
import psycopg2
  
def connectPostgreSQL():
    conn = psycopg2.connect(database="postgres", user="postgres", password="R011638q", host="127.0.0.1", port="5432")
    print('connect successful!')

if __name__=='__main__':
    connectPostgreSQL(i)