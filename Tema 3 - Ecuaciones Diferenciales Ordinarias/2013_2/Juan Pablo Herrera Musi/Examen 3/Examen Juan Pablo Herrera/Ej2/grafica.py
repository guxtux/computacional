##module grafica
from numpy import *
import matplotlib.pyplot as plt

def graffun(f,min,max):
    x=linspace(min,max,50)
    y=[]
    for t in x:
        y.append(f(t))
    plt.plot(x,y)
    plt.hold(True)

def grafpto(x,y):
    plt.plot(x,y,"s")
    plt.hold(True)

def grafvector(x,y,nombre):
    if len(x)!=len(y):
        t=linspace(x[0],x[1],len(y))
    else:
        t=x
    plt.plot(t,y,label=nombre)
    plt.legend(loc="best")
    plt.hold(True)

def titulos(titulo,x,y):    
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(titulo)
    plt.legend(loc="best")
    plt.hold(True)

def ejes(x,y):
    plt.axis(x+y)
    plt.hold(True)
    
def muestra():
    plt.grid()
    plt.show()
    
    
