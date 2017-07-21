from heatmappy import Heatmapper
from PIL import Image

x = []
y = []
for line in open('test.csv'):
    _list = line.split(",")
    temp_x = float(_list[0])
    temp_y = float(_list[1])
    x.append(temp_x)
    y.append(temp_y)

points = [x, y]
img_path = '001.jpg'
img = Image.open(img_path)

heat_mapper = Heatmapper()
heat_map = heat_mapper.heatmap_on_img(points, img)
heat_map.save('heat_map.png')
