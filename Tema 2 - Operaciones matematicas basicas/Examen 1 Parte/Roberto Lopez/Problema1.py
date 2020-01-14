from numpy import *
from neville import *
xd=array([-1.2,0.3,1.1])
yd=array([-5.76,-5.61,-3.69])
print "a) Utiizando el metodo de Neville:",neville(xd,yd,0.0)
n=2
x=array([-1.2,0.3,1.1])
f=array([-5.76,-5.61,-3.69])
x0=[0.0]
for k in x0:
    yres=0
    for i in range(0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i != j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i] 
    print 'b) Utilizando el metodo de Lagrange: El polinomio evaluado en P(',k,')= ',yres
