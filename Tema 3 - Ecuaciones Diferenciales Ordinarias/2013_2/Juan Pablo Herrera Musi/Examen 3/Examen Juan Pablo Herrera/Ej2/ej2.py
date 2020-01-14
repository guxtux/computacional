
from ecdif import *
from numpy import *
from grafica import *
#un deposito conico con 0.5m de altura de agua
#en el fondo tiene un orificio de 0.02m de radio

#el radio del deposito esta dado por r=0.25y    ;y-->altura
#la velocidad del agua que sale es   v^2=2gy



#cuantos minutos se tardará en vaciar

def df(y,v,t):
    g=9.81
    return -sqrt(2*g*y)

def vol(y,v,t):
    r=0.25*y
    return (((0.25**2)/.02)*(y**3))



h=0.001
intervalo=[0,10]
y0=0.5
v0=0

f,t,v=euler(vol,df,h,intervalo,y0,v0)
i=0
for a in t:
    t[i]=a*1000/60
    i=i+1

grafvector(t,f,"El cono se vacia en t=%2.2f(min)"%(t[i-1]))
titulos("Salida del agua","tiempo(seg)","Altura (m)")
xmax=t[len(t)-1]+t[len(t)-1]*.2
ejex=[0,xmax]
ejey=[0,.6]
ejes(ejex,ejey)
muestra()
