# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:49:30 2018

@author: VP LAB
"""

from scipy.special import gamma as Gamma
#from scitools.std import *
from pylab import *

def f1(x):
    return Gamma(x)


x = linspace(-6, 6,100)
y1 = f1(x)

# Matlab-style syntax:
plot(x, y1)

xlabel('x')
ylabel('y')
# legend(r'$\Gamma(x)$')
axis([-6, 6, -100, 100])
grid(True)

show()
