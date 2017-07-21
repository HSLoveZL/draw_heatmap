# -*-coding:utf8-*-
import csv
import matplotlib.pyplot as plt

arr = []
with open('test.csv') as f:
    f_csv = csv.reader(f)  # 读取文件内容
    for val in f_csv:
        arr.append(val)

x = []
y = []

for v in arr[1:]:
    axisX = float(v[0])
    axisY = float(v[1])
    x.append(axisX)
    y.append(axisY)
    plt.scatter(x, y)
    plt.plot(x[0:], y[0:], 'r')
plt.savefig("test.png", dpi=160)
plt.show()
