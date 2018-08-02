# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 10:21:58 2018

@author: VP LAB
"""


import math
import matplotlib.pyplot as plt
import numpy as np

def L(x):
    a = []
   # c=100
    #a1=2
    for item in x:
               #(the sigmoid function)
        a.append(max(0,(1-item**2)**(1/2.0)))
    return a
x = np.arange(-10, 50, 0.5)
y = L(x)
plt.plot(x,y)
plt.show() 
