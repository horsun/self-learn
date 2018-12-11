import numpy as np
import matplotlib.pyplot as plt

x, y = [], []
f = open('house_prices.txt', 'r').readlines()
for each in f:
    each = each.split(',')
    x.append(float(each[0]))
    y.append(float(each[1].strip()))
x, y = np.array(x), np.array(y)
# mean() 平均值
# std()  标准差
x = (x - x.mean()) / x.std()
print(x)
# 将原始数据集以散点的形式画出
plt.figure()
plt.scatter(x, y, c="g", s=6)
plt.show()
