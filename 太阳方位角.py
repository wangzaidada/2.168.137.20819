# -*- coding:utf-8 -*-
"""
作者：DUAN
日期：2022年06月02日
"""
import math
import datetime
from math import pi


def solar_azimuth(time, E, F):
    d = datetime.datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S')
    # minute, second = math.modf((120 - E) * 4)
    # second = math.modf(second * 60)[1]
    # d = d - datetime.timedelta(minutes=minute, seconds=second)
    t = d.hour + d.minute / 60 + d.second / 3600 + (E-120)/15
    w = (t - 12) * 15
    print(w)
    n = (d - datetime.datetime(year=d.year, month=1, day=1, hour=0, minute=0, second=0)).days
    sinδ = 0.39795 * math.cos(0.98563 * (n - 173) / 180 * pi)
    o = sinδ/pi * 180
    sinhs = math.sin(F)*math.sin(o) + math.cos(F)*math.cos(o) * math.cos(w)
    hs = sinhs/pi * 180
    print(hs)
    cosAS = sinhs*math.sin(F)-sinδ/(math.cos(hs)*math.cos(F))
    print(sinhs)
    print(cosAS)

    return


print(solar_azimuth('2019-10-08 10:20:00', 115.78388, 40.34924))
