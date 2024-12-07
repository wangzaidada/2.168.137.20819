# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月25日
"""

ls = [['北京', '上海', '广州'], ["'123", "'123", "123"], ["123", "123", "123"]]
f = open('123.csv', 'x+')
for item in ls:
    f.write(','.join(item)+'\n')
f.close()
