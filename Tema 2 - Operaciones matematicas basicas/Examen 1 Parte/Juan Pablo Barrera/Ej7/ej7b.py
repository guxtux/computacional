from falsaposicion import *
from numpy import *
from grafica import *

def f(x):
    fx=log(1+x)-x**2
    return fx


a,c=-.8,10
n=10
dx=.01
graffun(f,a,3)

raiz=[]
x1,x2=buscaraiz(f,a,c,dx)
i=1

while x1!=x2:
    raiz.append(falsaposicion(f,x1,x2,n))
    a=raiz[i-1]+dx
    x1,x2=buscaraiz(f,a,c,dx)
    
    
    i=i+1

print("la funcion tiene",len(raiz),"raices")
for i in raiz:
    print("La funcion tiene una raiz en x=%3.5f"%i)
    grafpto(i,0)

muestra()
