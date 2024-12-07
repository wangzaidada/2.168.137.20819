# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年05月30日
"""
# CalHamletV1.py


def gettext():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   # 将文本中特殊字符替换为空格
    return txt


hamletTxt = gettext()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1  # 赋初值为零每次进行加一操作
items = list(counts.items())    # 将字典类型转换成元组类型，接着将元组类型转换成列表类型
items.sort(key=lambda x: x[1], reverse=True)    # 以列表的每列的第二个元素为键值排序，True为从大到小排序
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))  # word向左对齐宽度为10格，count向右对齐宽度为5格

