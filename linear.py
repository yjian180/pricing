# -*- coding: utf-8 -*-
# @Time    :2018/7/13 23:05
# @Author  :jian y
# @File    : linear.py
# @Software: PyCharm

import numpy as np
from sklearn import datasets, linear_model

diabets = datasets.load_diabetes()

diabets_X = diabets.data[:, np.newaxis, 2]

diabets_X.train = diabets_X[:, 20]
diabets_X.test = diabets_X[:, 20]

diabets_y_train = diabets.target[:]

