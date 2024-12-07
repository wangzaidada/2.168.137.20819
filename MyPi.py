# main.py
import random
circle = 0
n = eval(input())
random.seed(123)
for i in range(n):
    x, y = random.random(), random.random()
    r = pow((x*x+y*y), 0.5)
    if r <= 1:
        circle += 1
# python中不支持自增符"++"
pi = 4*(circle/n)
print("{:.6f}".format(pi))
