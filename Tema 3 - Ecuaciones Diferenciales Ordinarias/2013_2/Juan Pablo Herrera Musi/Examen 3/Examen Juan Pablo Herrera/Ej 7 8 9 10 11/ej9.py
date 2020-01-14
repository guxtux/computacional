from ruku3 import *
from grafica import *
c=.005
g=9.9
h=.1

def V(x):
    return sqrt((x[0]**2)+(x[1]**2))

def f(x,t):
    F=[]
    F.append(h*(-c*V(x)*x[0]))
    F.append(h*(-g-c*V(x)*x[1]))
    return F

y0=[150,150]
velocidades,t=rk3(f,y0,0,h)#aplico rk3 para encontrar las velocidades
def trayecto(x,t):
    T=[]
    T.append(h*velocidades[int(t/h)][0])
    T.append(h*velocidades[int(t/h)][1])
    return T


T0=[0,0]
trayectoria,t=rk3(trayecto,T0,0,h)#vuelvo a usar rk3 para las posiciones

x=[]
y=[]
i=0
while trayectoria[i][1]>=0:
    x.append(trayectoria[i][0])
    y.append(trayectoria[i][1])
    i=i+1

grafvector(x,y,"trayectoria del proyectil")

titulos("trayectoria","x (m)","y(m)")
muestra()

