#! usr/bin/env python3
# -*- coding:utf-8 -*-

# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

__author__ = 'jqbk'
__date__ = '2017-06-22'

import re

def count_words():
    pattern = re.compile(r'\w+')

    with open ('E:\\Software-Docs\\python_documents\\python-exercise\\play4\\article.txt', 'r') as f:
        words = pattern.findall(f.read())
        cnt = len(words)

    print('This article have {0:^6d} words.'.format(cnt))

if __name__ == '__main__':
    count_words()