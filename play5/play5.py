#! usr/bin/env python3
# -*- coding:utf-8 -*-

# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

__author__ = 'jqbk'
__date__ = '2017-06-22'

import os
from PIL import Image

def change():
    path = 'E:\\Software-Docs\\python_documents\\python-exercise\\play5\\背景图片\\'
    os.chdir(path)
    pics = os.listdir(path)

    for pic in pics:
        im = Image.open(pic)
        im = im.convert('RGB')
        w, h = im.size
        # pic_format = im.format
        while w > 640 or h > 1136:
            w = 640
            h = 1136
            im.thumbnail((w, h))
            pic_newname = pic.split('.')[0] + 'jq.jpg'
            im.save(pic_newname, 'JPEG')
    print('All pictures are changed!')

if __name__ == '__main__':
    change()