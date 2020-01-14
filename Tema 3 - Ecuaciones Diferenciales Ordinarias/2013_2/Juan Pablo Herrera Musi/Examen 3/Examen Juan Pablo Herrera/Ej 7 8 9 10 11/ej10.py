from ruku3 import *
from grafica import *

M=5.#kg
k=3.2#kg/s2
w=(k/M)**2#1/s
amt=0.5#c/2 M w
h=.05
A=2*amt*w
B=w*w

def fuerza(t):
    if t<=1:
        return 1.
    else:
        return 0

def f(x,t):
    F=[]
    F.append(h*(x[1]))
    F.append(h*(-A*x[1]-B*x[0]+fuerza(t)/M))
    return F

y0=[0,0]
res,t=rk4(f,y0,10,h)
pos=[]
vel=[]
i=0
for a in res:
    pos.append(a[0])
    vel.append(a[1])
    

grafvector(t,pos,"Movimiento del carrito")
titulos("Carrito sujeto a resorte F=1 durante 1 seg","tiempo (seg)","posicion(respecto al equilibrio)")
muestra()

