# main.py
height, weight = eval(input())
# 输入默认为字符串"12,12"用eval去除""变为列表类型
BMI = weight/pow(height, 2)
if BMI < 18.5:
    JB = "偏瘦"
    NB = "偏瘦"
elif BMI < 24:
    JB = "正常"
    NB = "正常"
elif BMI < 25:
    JB = "正常"
    NB = "偏胖"
elif BMI < 28:
    JB = "偏胖"
    NB = "偏胖"
elif BMI < 30:
    JB = "偏胖"
    NB = "肥胖"
else:
    JB = "肥胖"
    NB = "肥胖"
print("BMI数值为:{:0.2f}".format(BMI))
print("BMI指标为:国际'{}',国内'{}'".format(JB, NB))
