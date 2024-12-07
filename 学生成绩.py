# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年06月01日
"""
import numpy as np
import pandas as pd

d1 = {"name": ["A", "B", "C", "D"],
      "C": [70, 60, 90, 50],
      "JAVA": [80, 40, 80, 80],
      "C++": [50, 90, 80, 50],
      "Python": [60, 70, 60, 80],
      "C#": [80, 60, 90, 70]
      }
sc = {
    # 名称 : (C,JAVA,C++,Python,C#)
    'A': (70, 80, 50, 60, 80),
    'B': (60, 40, 90, 70, 60),
    'C': (90, 80, 80, 60, 90),
    'D': (50, 80, 50, 80, 70)
}
# t = pd.DataFrame([(70, 80, 50, 60, 80),
#                   (60, 40, 90, 70, 60),
#                   (90, 80, 80, 60, 90),
#                   (50, 80, 50, 80, 70)], index=["A", "B", "C", "D"], columns=["C", "JAVA", "C++", "Python", "C#"])
t = pd.DataFrame(d1)
print(t.max())
# for i in sc:
#     print(i, max(sc[i]), min(sc[i]), sum(sc[i]) / len(sc[i]))
