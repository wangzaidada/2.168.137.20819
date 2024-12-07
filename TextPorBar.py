# TextPorBar.py
import time
str1 = "执行开始"
str2 = "执行结束"
print(str1.center(26, '-'))
time1 = time.perf_counter()
for i in range(51):
    a = i * 2
    b = '*' * i
    c = b + '->'
    time2 = time.perf_counter()
    print("\r{:3}%[{:-<52}]{:0.2}s".format(a, c, time2 - time1), end='')
    time.sleep(0.1)
print("\n"+str2.center(26, '-'))
