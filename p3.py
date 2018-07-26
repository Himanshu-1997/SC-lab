# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:43:17 2018

@author: VP LAB
"""

import matplotlib.pyplot as plt
y=list()
x=list(range(-10,10))
for i in x:
    y.append(1/(1+(i*i)))
  
plt.plot(x,y)
 

plt.xlabel('x - axis')

plt.ylabel('y - axis')
 

plt.title('y=1/(1+x^2)')
 

plt.show()
