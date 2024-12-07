# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2021年10月25日
"""
"""
r:只读（文件不存在返回FileNotFoundError）
w:覆盖写模式，文件不存在则创建，存在则完全覆盖
x:创建写模式，文件并不存在则创建，存在则返回FileExistsError
a:追加写模式，文件不存在则创建，存在则在文件最后追加内容
b:二进制文件模式
t:文本文件模式
+:与r/w/x/a一同使用在原功能的基础上增加同时读写功能
"""
f = open("wj.txt", 'w+')  # w+可以实现读写同时进行r+,x+,a+
ls = ["中国", "法国", "美国"]
f.writelines(ls)
f.seek(0)
for i in f:
    print(i)
f.close()
