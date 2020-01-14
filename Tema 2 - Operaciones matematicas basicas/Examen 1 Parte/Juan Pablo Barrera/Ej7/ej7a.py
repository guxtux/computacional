from falsaposicion import *
from numpy import *
from grafica import *

def f(x):
    fx=0.5*exp(x/3)-sin(x)
    return fx


a,c=0,10
n=10
dx=1
graffun(f,a,5)

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
    print("La funcion tiene una raiz en x=",i)
    grafpto(i,0)

muestra()
