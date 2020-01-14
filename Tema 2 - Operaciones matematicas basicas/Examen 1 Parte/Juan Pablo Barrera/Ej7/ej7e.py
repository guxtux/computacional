# -*- coding: cp1252 -*-
from falsaposicion import *
from numpy import *
from grafica import *

def f(x):
    fx=sqrt(x+2)
    return fx

x=linspace(-2,10)

plt.plot(x,f(x))
l=plt.axhline(y=0.0 ,color='k', linestyle ='-')
s=plt.axvline(x=0.0 ,color='k', linestyle ='-')
plt.title(ur'Función $\sqrt{x+2}$',fontsize=20)
plt.ylabel("f(x)")
plt.grid(1)
plt.ylim(ymin=-0.5)
plt.xlim(xmin=-2.5)
plt.show()

a,c=-2,10
n=10
dx=.1
graffun(f,-10,c)
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
