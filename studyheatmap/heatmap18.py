# -*-coding:utf8-*-
import numpy as np
import matplotlib.pyplot as plt
import sphviewer as sph


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


def my_plot(x, y, nb=32, xsize=500, ysize=500):
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)

    x0 = (x_min+x_max)/2
    y0 = (y_min+y_max)/2

    pos = np.zeros([3, len(x)])
    pos[0, :] = x
    pos[1, :] = y
    w = np.ones(len(x))

    p = sph.Particles(pos, w, nb=nb)
    s = sph.Scene(p)
    s.update_camera(r='infinity', x=x0, y=y0, z=0,
                    xsize=xsize, ysize=ysize)
    r = sph.Render(s)
    r.set_logscale()
    img = r.get_image()
    extent = r.get_extent()
    for i, j in zip(xrange(4), [x0, x0, y0, y0]):
        extent[i] += j
    print extent
    return img, extent


if __name__ == "__main__":
    csv_file_name = "test.csv"
    _x, _y = get_data(csv_file_name)
    my_plot(_x, _y)

    fig = plt.figure(1, figsize=(10, 10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    # Plotting a regular scatter plot
    ax1.plot(_x, _y, 'k.', markersize=5)
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)

    heat_map_16, extent_16 = my_plot(_x, _y, nb=16)
    heat_map_32, extent_32 = my_plot(_x, _y, nb=32)
    heat_map_64, extent_64 = my_plot(_x, _y, nb=64)

    ax2.imshow(heat_map_16, extent=extent_16, origin='lower', aspect='auto')
    ax2.set_title("Smoothing over 16 neighbors")

    ax3.imshow(heat_map_32, extent=extent_32, origin='lower', aspect='auto')
    ax3.set_title("Smoothing over 32 neighbors")

    # Make the heat_map using a smoothing over 64 neighbors
    ax4.imshow(heat_map_64, extent=extent_64, origin='lower', aspect='auto')
    ax4.set_title("Smoothing over 64 neighbors")

    plt.show()
