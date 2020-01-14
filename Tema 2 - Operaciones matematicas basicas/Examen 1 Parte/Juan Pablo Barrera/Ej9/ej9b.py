from secante import *
from numpy import *
from grafica import *
def f(x):
    fx= -0.2*x**2 +1 +log(x)
    return fx


a=0.02
b=10
i=0
graffun(f,a,b)
x1=a
x2=b
dx=.01
print("     Intervalo     raiz")
print("-----------------------")
x1,x2=buscaraiz(f,x1,b,dx)
while x1!=x2:
    raiz=secante(f,x1,x2,.001)
    print(" %2.3f %2.3f    x=%2.5f"%(x1,x2,raiz))
    grafpto(raiz,0)
    x1=x2
    x1,x2=buscaraiz(f,x1,b,dx)
muestra()
