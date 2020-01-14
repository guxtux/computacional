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

def muestra():
    plt.grid()
    plt.show()
    
    
