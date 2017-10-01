#! usr/bin/env python3
# -*- coding:utf-8 -*-

# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

__author__ = 'jqbk'
__date__ = '2017-06-17'

from PIL import Image, ImageDraw, ImageFont

def add_num(pic, num):
    img = Image.open(pic)
    width, height = img.size
    myfont = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', size=height//4)
    ImageDraw.Draw(img).text((width-width//8,0), str(num), fill=(255,0,0), font=myfont)
    img.save('E:\\Software-Docs\\python_documents\\python-exercise\\play0\\pic_with_num.jpg', 'jpeg')

if __name__ == '__main__':
    add_num('E:\\Software-Docs\\python_documents\\python-exercise\\play0\\weixin.png', 7)