# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:15:11 2018

@author: VP LAB
"""

import numpy as np
from scipy.integrate import simps, trapz
import matplotlib.pyplot as plt

def f(x):
    return x**2

fig, ax = plt.subplots(1,1)

#Continous curve
x=np.arange(0,9,0.01)
y=f(x)
ax.plot(y,x, 'k-')




plt.show()
