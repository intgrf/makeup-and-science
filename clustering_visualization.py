import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

np.random.seed(20)

# задаем координаты и изображения
x = np.arange(100)
y = np.random.rand(len(x))
arr = np.zeros((len(x), 10, 10))

# создаем figure и отрисовываем scatter plot
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x, y, ls="", marker="o")

# создаем annotation box
im = OffsetImage(arr[0, :, :], zoom=5)
xybox = (50., 50.)
ab = AnnotationBbox(im, (0, 0), xybox=xybox, xycoords='data', boxcoords="offset points",  pad=0.3,  arrowprops=dict(arrowstyle="-"))
# add it to the axes and make it invisible
ax.add_artist(ab)
ab.set_visible(False)


def hover(event):
    # если курсор поверх точки на графике
    if line.contains(event)[0]:
        # ищем индекс точки
        ind, = line.contains(event)[1]["ind"]
        # размер изображения
        w, h = fig.get_size_inches()*fig.dpi
        ws = (event.x > w/2.)*-1 + (event.x <= w/2.)
        hs = (event.y > h/2.)*-1 + (event.y <= h/2.)
        # если точка наверху и справа, меняем позицию annotation box
        ab.xybox = (xybox[0]*ws, xybox[1]*hs)
        ab.set_visible(True)
        ab.xy = (x[ind], y[ind])
        # показываем нужную картинку
        im.set_data(arr[ind, :, :])
    else:
        # если курсор не поверх точки на графике
        ab.set_visible(False)
    fig.canvas.draw_idle()


fig.canvas.mpl_connect('motion_notify_event', hover)
plt.show()
