# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#a = input("Input a :  ")
#ma = input(")

a={}
b={}
print("Enter the number of inputs in A :")
m=int(input())

print("Enter the number of inputs in B :" )
n=int(input())

print("Enter the elememts in A")

for i in range(0,m):
  k,v=input().split( )
  a[int(k)]=float(v)
  
print("Enter the elememts in B")
for i in range(0,n):
  k,v=input().split( )
  b[int(k)]=float(v)
  
union={}



for  k1,v1 in a.items():
  for k2,v2 in b.items():
    v=-1
    if(k1==k2):
      v=max(v1,v2)
      union[k1]=v
    else:
      union[k1]=v1
      if(union.get(k2)==None):
       union[k2]=v2
    
print("UNION")
      
for  k1,v1 in union.items():
    print(k1,v1)
    
intersection={}

for  k1,v1 in a.items():
  for k2,v2 in b.items():
    v=-1
    if(k1==k2):
      v=max(v1,v2)
      intersection[k1]=v
    
print("Intersection")
    
for  k1,v1 in intersection.items():
    print(k1,v1)

ComplimentofA={}

for k,v in a.items():
  ComplimentofA[k]=1-v;
  
print("Compliment of A:")
for  k1,v1 in ComplimentofA.items():
    print(k1,v1)
  
ComplimentofB={}

for k,v in b.items():
  ComplimentofB[k]=1-v;
print("Compliment of B:")
for  k1,v1 in ComplimentofB.items():
    print(k1,v1)
