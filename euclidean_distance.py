# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:20:34 2018

@author: VP LAB
"""

import numpy as np

x=[]
for i in range(4):
    a=float(input())
    x.append(a)
y=[]
for i in range(4):
    a=float(input())
    y.append(a)
p=np.array(x)
q=np.array(y)
dist=np.linalg.norm(p-q)
print(dist)
