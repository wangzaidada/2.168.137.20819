# def f(x):
#     for i in range(2, x+1):
#         if x == i:
#             print(i)
#             return
#         if x % i == 0:
#             f(x // i)
#             print(i)
#             return
def f(x):
    for i in range(2, x):
        if x % i == 0:
            t = f(x//i)  # 递归，直到运行到最后一个质数时才进行赋值
            t.append(i)  # 添加进列表
            return t     # 结束运行
    return [x]  # 返回一个列表类型的质数用于t的赋值


v = int(input())
print(f(v)[::-1])  # 最终结果为倒序
