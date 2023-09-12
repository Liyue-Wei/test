# coding=utf-8
# 3D心形

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False


def heart_3d(x, y, z):
    return (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3


def plot_implicit(fn, bbox=(-1.5, 1.5)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 200)    # 轮廓分辨率
    B = np.linspace(xmin, xmax, 80)     # 切片数量
    A1, A2 = np.meshgrid(A, A)          # 绘制等高线的网格

    for z in B:     # 在XY平面绘制等高线
        X, Y = A1, A2
        Z = fn(X, Y, z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z', colors=('r',))

    for y in B:     # 在XZ平面绘制等高线
        X, Z = A1, A2
        Y = fn(X, y, Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y', colors=('red',))

    for x in B:     # 在YZ平面绘制等高线
        Y, Z = A1, A2
        X = fn(x, Y, Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors=('red',))

    ax.set_zlim3d(zmin, zmax)
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)
    # 标题
    plt.title("I love you", fontsize=30)
    # 取消坐标轴显示
    plt.axis('off')
    # 保存文件
    plt.savefig("3D_❤图.png")  # 在 plt.show() 之前调用 plt.savefig()
    plt.show()


if __name__ == '__main__':
    plot_implicit(heart_3d)
