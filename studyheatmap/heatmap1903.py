# -*-coding:utf8-*-
import csv
import matplotlib.pyplot as plt

arr = []
with open('test.csv') as f:
    f_csv = csv.reader(f)
    for val in f_csv:
        arr.append(val)
x = []
y = []
for v in arr[1:]:
    axisX = float(v[0])
    axisY = float(v[1])
    x.append(axisX)
    y.append(axisY)
    plt.scatter(axisX, axisY)
    plt.plot(x, y, 'r')
plt.show()
