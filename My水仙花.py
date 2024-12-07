# main.py
flag = 1
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            x = eval(str(i)+str(j)+str(k))
            y = pow(i, 3) + pow(j, 3) + pow(k, 3)
            if x == y:
                if flag == 1:
                    print("{}".format(x), end="")
                    flag = 0
                else:
                    print(",{}".format(x), end="")

