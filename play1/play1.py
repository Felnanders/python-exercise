#! usr/bin/env python3
#  -*- coding:utf-8 -*-

# 第 0001 题：作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

__author__ = 'jqbk'
__date__ = '2017-06-18'

import random, string

def coupon(num, length):
    chars = string.digits + string.ascii_letters
    with open('E:\\Software-Docs\\python_documents\\python-exercise\\play1\\coupon.txt', 'w') as f:
        for i in range(num):
            code = [random.choice(chars) for i in range(length)]
            f.write(''.join(code) + '\n')

if __name__ == '__main__':
    coupon(200, 7)