import time
sentence = input()
long = len(sentence)
a1 = "abcdefghijklmnopqrstuvwxyz"
a2 = "defghijklmnopqrstuvwxyzabc"
A1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A2 = "DEFGHIJKLMNOPQRSTUVWXYZABC"
start = time.perf_counter()
for i in range(long):
    t = sentence[i]
    if t in a1:
        x = a1.index(t)
        print("{}".format(a2[x % 26]), end='')
    elif t in A1:
        x = A1.index(t)
        print("{}".format(A2[x % 26]), end='')
    else:
        print("{}".format(t), end='')
end = time.perf_counter()
run_time = end-start
print("\n转换时间为：" + "{0}".format(run_time))
