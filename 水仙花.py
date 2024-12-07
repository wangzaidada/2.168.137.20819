# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年06月01日
"""
for i in range(100, 1000):
    a = str(i)
    b = int(a[0])  # 百位
    c = int(a[1])  # 十位
    d = int(a[2])  # 个位
    e = pow(b, 3) + pow(c, 3) + pow(d, 3)
    if i == e:
        print(i)

