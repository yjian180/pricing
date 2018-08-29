# -*- coding: utf-8 -*-
# @Time    :2018/6/30 16:04
# @Author  :jian y
# @File    : pricing.py
# @Software: PyCharm

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

figure = plt.figure()
ax = Axes3D(figure)
X = np.arange(0, 1, 0.02)
Y = np.arange(0, 1, 0.02)

#a = np.arange(0, 1, 0.02)
#网格化数据
X, Y = np.meshgrid(X, Y)

Z = 2 * Y**0.5 * (X - 0.5*X**2)

#Z = (X**0.5) * (Y**2-1)
#Z = X**0.5 * (Y**0.5)

#Z = X + Y*(1-X)
# R = np.sqrt(X**2 + Y**2)
# Z = np.cos(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()