# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年06月01日
"""
import math

a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
if a != 0:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("无根")
    elif delta == 0:
        s = -b / (2 * a)
        print("唯一根x=", '%.2f' % s)
    else:
        root = math.sqrt(delta)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)
        print("x1=", '%.2f' % x1)
        print("x2=", '%.2f' % x2)
