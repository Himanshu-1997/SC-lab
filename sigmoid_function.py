# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:50:18 2018

@author: VP LAB
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    a = []
    for item in x:
               #(the sigmoid function)
        a.append(1/(1+math.exp(-item)))
    return a
x = np.arange(-10., 10., 0.2)
y = sigmoid(x)
plt.plot(x,y)
plt.show()
