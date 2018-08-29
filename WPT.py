# -*- coding: utf-8 -*-
# @Time    :2018/7/11 23:31
# @Author  :jian y
# @File    : WPT.py
# @Software: PyCharm


from matplotlib import pyplot as plt
import numpy as np

# from pylab import * #导入pylab，构建类似于MATLAB的环境

x = np.arange(0, 1, 0.01)

cond = [True if (i>=0.15 and i<= 0.55) else False for i in x] #使用列表解析的方法

y = 0 * (x < 0.15) + (2 * ((x-0.15)/0.85) ** 2) * cond + (1 - 2*((1-x)/0.85)**2) * (x > 0.55)

plt.xlabel("t")
plt.ylabel("y")
plt.title("Heavsine")
plt.plot(x, y, 'r', lw =4)
plt.show()

print(x, y)