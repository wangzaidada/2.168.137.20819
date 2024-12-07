# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月25日
"""
f = open('hamlet.txt', "r")
print(f.read(4))    # 读入全部内容，如果给出参数，读入前size长度
print(f.readline(-1))   # 读入一行内容，如果给出参数，读入前size行
print(f.readlines(1))    # 读入文件所有行，以每行为元素形成【列表】，如果给出参数，读入前hint行
f.close()
