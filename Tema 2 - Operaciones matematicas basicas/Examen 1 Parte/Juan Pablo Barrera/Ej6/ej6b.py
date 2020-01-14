from bisecccion import *
from numpy import *
from grafica import *
def f(x):
    fx=sin(x)-0.3*exp(x)
    return fx



a=0
dx=pi/100
b=300
graffun(f,a,2)

x1=a
raiz=[]
while x1<b:
    x1,x2=buscaraiz(f,x1,b,dx)
    if abs(f(x1))<100 and abs(f(x2))<100 and x1<b: #criterio para que omita las raices "fantasma"
        raiz.append(bisect(x1,x2,1,0.0001,f))
    x1=x2

print("la funcion tiene",len(raiz),"raices")
print("en los siguientes valores de x f(x)=0")
for i in arange (len(raiz)):
    print("x=%2.5f"%(raiz[i]))
    grafpto(raiz[i],0)

muestra()


