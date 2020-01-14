# constates matematicas
"""
Created on Wed Sep  5 00:58:54 2012

@author: usuario
"""
# calculo de pi
n=0
p=0
while n<1000:
    p=p+((-1.)**n)*(1./(2*n+1))
    n=n+1
    
    
p1=4*p
print "el valor aproximado de pi es p=%.3f " %(p1)

# calculo de e
x=2
z=1
while z<2:
    x=x+1
    z=z+1
    e=2+1./x*z
print "el valor de e=%.3f " %(e)

# calculo de la cte. de euler
from math import log 
x=1
ga=0
while x>0:
    ga=1+1/x-log(x)
    x=x-1
print "el valor de gama es %.3f " %(ga)