from secante import *
from numpy import *
from grafica import *
def f(x):
    fx=0.1*x**3 -5*x**2 -x +4 +exp(-x)
    return fx


a=-10
b=100
graffun(f,a,51)
i=0
x1=a
x2=b
dx=.1
print("     Intervalo     raiz")
print("-----------------------")
x1,x2=buscaraiz(f,x1,b,dx)
while x1!=x2:
    raiz=secante(f,x1,x2,.001)
    print("%2.3f %2.3f    x=%2.5f"%(x1,x2,raiz))
    grafpto(raiz,0)
    x1=x2
    x1,x2=buscaraiz(f,x1,b,dx)

muestra()
