# polinomio de grado 4
"""
Spyder Editor

This temporary script file is located here:
/home/usuario/.spyder/.temp.py
"""
A=(48,100,70,-20,2)
b=A[4]
n=4
C=[]
x=[-4,-3.5,-3,-2.5,-2,-1.5,-1]
for i in range(len(x)):
    while n>0:
       n=n-1
       b=A[n]+x[i]*b
C.append(b)
print C