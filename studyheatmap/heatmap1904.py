# -*-coding:utf8-*-
import csv
import numpy as np
import matplotlib.cm as cm
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

heatmap, xedges, yedges = np.histogram2d(x, y, bins=16)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
img = plt.imread('001.jpg')
plt.clf()
plt.imshow(heatmap.T, interpolation='sinc', cmap=cm.get_cmap('rainbow', 1000),
           extent=extent, aspect='auto', origin='lower')
plt.axis('off')
plt.colorbar()
plt.savefig("test_heat_map6.png", dpi=132)
plt.show()
