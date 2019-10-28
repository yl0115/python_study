# -*- coding:utf-8 -*-
from PIL import Image


im = Image.open(r'e:\永川1\梁家成_18980454423.jpg')
width = im.size[0]
height = im.size[1]
print(width)
print(height)
a = im.resize((width//10, height//10))
a.save(r'e:\永川1\梁家成_18980454423.jpg')
