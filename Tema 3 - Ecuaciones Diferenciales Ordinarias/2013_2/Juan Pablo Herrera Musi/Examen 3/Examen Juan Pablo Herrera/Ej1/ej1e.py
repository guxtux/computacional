from grafica import *
from ecdif import *

def df(y,t):
    df= -sqrt(abs(y))+sin(t)
    return df

y0=1
h=0.01
intervalo=[0,5]
sol,t=euler(df,h,intervalo,y0)

grafvector(t,sol,"y'+(abs(y))^1/2=sin(t)")
titulos("y'+(abs(y))^1/2=sin(t)","t","y(t)")
muestra()
