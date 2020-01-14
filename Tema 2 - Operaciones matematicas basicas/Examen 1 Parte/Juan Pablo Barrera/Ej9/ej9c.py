from secante import *
from numpy import *
from grafica import *
def f(x):
    dx=.1
    if x==-3 or x==0:
        return 0
    fx= x+(1/(x*(x+3)))
    return fx


a=-10
b=10
graffun(f,-4,1)
i=0
x1=a
x2=b
dx=.01
print("     Intervalo     raiz")
print("-----------------------")
x1,x2=buscaraiz(f,x1,b,dx)
while x1!=x2:
    raiz=secante(f,x1,x2,.001)
    if abs(f(raiz))<1:
        print(" %2.3f %2.3f    x=%2.5f"%(x1,x2,raiz))
        grafpto(raiz,0)
    x1=x2
    x1,x2=buscaraiz(f,x1,b,dx)
muestra()
