# problema 3,lista 3, velocidad angular
"""
@author: Calderon Apolinar Marco A
"""
from math import sin,cos,sqrt
x=range(0,181,5)

def pos(o):
    return 90*(cos(o)+sqrt(2.5**2-(sin(o))**2))

f=[]
for c in x:
    y=pos(c)
    f.append(y)
    
# para calcular la derivada
n=3
def g(xa):
 yres=0
 for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i!=j:
            z=z*(xa-x[j])/(x[i]-x[j])
    yres=yres+z*f[i]
 return yres

def d2f(r):
 h=0.087266
 w=(25e6)*(2*g(r)-5*g(r+h)+4*g(r+2*h)-g(r+3*h))/(h**2)
 return w
 
for l in x:
    print 'la aceleracion angular en',l,'grados es:', d2f(l)