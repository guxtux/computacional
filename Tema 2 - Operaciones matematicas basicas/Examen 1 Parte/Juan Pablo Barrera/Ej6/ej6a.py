from bisecccion import *
from numpy import *
from grafica import *

def f(x):
    fx=tan(x)-x+1
    return fx

a=0
b=3*pi
dx=pi/100
x1=a
raiz=[]
graffun(f,a,b)

while x1<b:
    x1,x2=buscaraiz(f,x1,b,dx)
    if abs(f(x1))<100 and abs(f(x2))<100 and x1<b: #criterio para que omita las raices "fantasma"
        raiz.append(bisect(x1,x2,1,0.0001,f))
    x1=x2

print("la funcion tiene",len(raiz),"raices")
print("en los siguientes valores de x f(x)=0")
for i in arange (len(raiz)):
    print("x=",raiz[i])
    grafpto(raiz[i],0)

muestra()


