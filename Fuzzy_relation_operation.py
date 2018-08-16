# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:14:40 2018

@author: VP LAB
"""
import numpy as np
def maxMin(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.minimum(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))

def maxProduct(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.multiply(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))

def compliment(x):
    z=[]
    for x1 in x:
        for y1 in x1:
            z.append(1-y1)
    return z

# 3 arrays for the example
#r1 = np.array([[0.7, 0.5], [0.8, 0.4]])
#r2 = np.array([[0.9, 0.6, 0.5], [0.1, 0.7, 0.5]])
m = int(input('number of rows, m : '))
n = int(input('number of columns, n : '))
a=[]
for i in range(1,m+1):
  b = []
  print("{0} Row".format(i))
  for j in range(1,n+1):
    b.append(float(input("{0} Column: " .format(j))))
  a.append(b)
print(a)
r1=np.array(a)
m = int(input('number of rows, m : '))
n = int(input('number of columns, n : '))
c=[]
for i in range(1,m+1):
  d = []
  print("{0} Row".format(i))
  for j in range(1,n+1):
    d.append(float(input("{0} Column: " .format(j))))
  c.append(d)
print(c)
r2=np.array(c)
print("\n\nRelation for Max-Min = max(min(x1,y),min(y,z1))\n\n")
print ("R1oR2 => Max-Min :\n" + str(maxMin(r1, r2)) + "\n\n")
print("\n\nRelation for MaxProd = Sum of((x1,y)*(y,z1))\n\n")
print ("\n\nR1oR2 => Max-Product :\n" + str(maxProduct(r1, r2)) + "\n\n")
print("\n\nRelation for complement = 1-x1\n")
print("Operation is performed on matrix A\n")
ans=compliment(a)
ans=np.array(ans).reshape((2, 2))
print(ans)
print("\n\n")
print("\n\nContainment operation of two matrices\n\n")
ma=0
mi=1
for x in a:
    for y in x:
      ma=max(y,ma)
      
for x in c:
    for y in x:
      mi=min(y,mi)
if(ma<mi):
    print("1")
else:
    print("0")
