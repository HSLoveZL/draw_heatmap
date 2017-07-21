from heatmappy import Heatmapper
from PIL import Image


def get_data(csv_file_path):
    """
    reader the csv file to draw the heat_map
    :param csv_file_path:
    :return:
    """
    x = []
    y = []
    for line in open(csv_file_path):
        _list = line.split(",")
        temp_x = float(_list[0])
        temp_y = float(_list[1])
        x.append(temp_x)
        y.append(temp_y)

    return x, y


def draw_heat_map(x, y):
    points = [x, y]
    img_path = '001.jpg'
    img = Image.open(img_path)

    heat_mapper = Heatmapper()
    heat_map = heat_mapper.heatmap_on_img(points, img)
    return heat_map.save('heat_map.png')


if __name__ == "__main__":
    csv_file_name = "test.csv"
    _x, _y = get_data(csv_file_name)
    draw_heat_map(_x, _y)
