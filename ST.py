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
while True:
    print("Press 1 for Euclidean Distance")
    print("Press 2 for Hamming Distance")
    print("Press 3 for Max-Min")
    print("Press 4 for Max-product")
    print("Press 5 for Containment")
    
    t=int(input())
    if(t==1):
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
        print("Euclidean distance between both set = ",end="")
        print(dist)
        
    elif(t==2):
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
    
    elif(t==3):
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
    
    elif(t==4):
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
        print("\n\nRelation for MaxProd = Sum of((x1,y)*(y,z1))\n\n")
        print ("\n\nR1oR2 => Max-Product :\n" + str(maxProduct(r1, r2)) + "\n\n")
    
    elif(t==5):
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
        print("\n\nContainment operation of two matrices is m1(x,y)<=m2(x,y)\n")
        ma=0
        mi=1
        for x in a:
            for y in x:
              ma=max(y,ma)
              
        for x in c:
            for y in x:
              mi=min(y,mi)
        if(ma<mi):
            print("Every element in matrix 1 is less than every element of 2nd matrix, so ans =  1\n")
        else:
            print("there is atleast one element in matrix 1 is greater than atleast one element of 2nd matrix,so ans = 0\n")

    
