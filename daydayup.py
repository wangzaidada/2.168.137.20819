# main.py

def up(f):
    base = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            base *= (1 - 0.01)
        else:
            base *= (1 + f)
    return base


origin = 0.01
while up(origin) < 37.78:
    origin += 0.001
print('{:.3f}'.format(origin))
