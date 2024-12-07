# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年06月01日
"""
# 一元二次函数图像
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-10, 10, 0.1)
y = x ** 2 - 7 * x + 1
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y)
plt.show()
