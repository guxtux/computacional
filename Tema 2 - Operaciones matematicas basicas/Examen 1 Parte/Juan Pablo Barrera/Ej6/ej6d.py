from bisecccion import *
from numpy import *
from grafica import *

def f(x):
    fx=16*x**5 -20*x**3 +x**2 +5*x -0.5
    return fx

a=0
dx=.01
b=1
x1=a
raiz=[]
graffun(f,a,b)
while x1<b:
    x1,x2=buscaraiz(f,x1,b,dx)
    if abs(f(x1))<100 and abs(f(x2))<100 and x1<b: #criterio para que omita las raices "fantasma"
        raiz.append(bisect(x1,x2,1,0.001,f))
    x1=x2

print("la funcion tiene",len(raiz),"raices")
print("en los siguientes valores de x f(x)=0")
for i in arange (len(raiz)):
    print("x=%2.3f"%(raiz[i]))
    grafpto(raiz[i],0)    

muestra()


