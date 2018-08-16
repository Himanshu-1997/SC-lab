# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 09:41:45 2018

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
z=[]
for i in range(4):
    a=float(abs(x[i]-y[i]))
    z.append(a)
dist=0
for i in range(4):
    dist+=float(z[i])
print("Hamming distance between both set = ",end="")
print(dist)
    
