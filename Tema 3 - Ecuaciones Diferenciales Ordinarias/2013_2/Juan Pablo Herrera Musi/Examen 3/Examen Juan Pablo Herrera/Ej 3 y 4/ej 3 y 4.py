from ecdif import *
from numpy import *
from grafica import *

def dv(x,v,t):
    g=9.81
    beta=0.
    return -2*g*x-beta*v

def dv2(x,v,t):
    g=9.81
    beta=0.8
    return -2*g*x-beta*v

def df(x,v,t):
    return x

y0=0.2
v0=0.
h=0.001
intervalo=[0,10]

y,t,v=euler(df,dv2,h,intervalo,y0,v0)
grafvector(intervalo,y,"beta=0.8")
y,t,v=euler(df,dv,h,intervalo,y0,v0)
grafvector(intervalo,y,"beta=0")
titulos("Movimiento del Agua dentro del tubo","tiempo(seg)","posicion(cm)")
muestra()
