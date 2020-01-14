from falsaposicion import *
from numpy import *
from grafica import *

def f(x):
    fx=x**3 +2*x -1
    return fx


a,c=-1,10
n=10
dx=.1
graffun(f,0,2)

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
