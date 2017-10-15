#! usr/bin/env pthon3
#  -*- coding:utf-8 -*-

# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

__author__ = 'jqbk'
__date__ = '2017-06-20'

import os
import sys
import psycopg2
  
def write_coupon():
    conn = psycopg2.connect(database="testdb", user="jqbk", password="R011638q", host="127.0.0.1", port="5432")
    print('connect successful!')

    cur = conn.cursor()
    cur.execute('SELECT tablename FROM pg_tables;')
    tablenames = cur.fetchall()

    # 判断表是否存在
    found = False
    if ('coupon',) in tablenames:
        found = True

    if not found:
        cur.execute('CREATE TABLE coupon(ID INTEGER, code VARCHAR(10));')
        print('creat table successfully!')
    
    with open('E:\\Software-Docs\\python_documents\\python-exercise\\play1\\coupon.txt', 'r') as f:
        content = f.readlines()
    
    for i in range(len(content)):
        cur.execute('INSERT INTO coupon(ID, code) \
                    VALUES(%s, %s);', (i+1, content[i])) # 占位符只能是%s
    
    conn.commit()

    cur.execute('SELECT * FROM coupon;')
    rows = cur.fetchall()
    for row in rows:
        print('ID = ', row[0])
        print('code = ', row[1], '\n')
    
    cur.close()
    conn.close()

if __name__=='__main__':
    write_coupon()