from grafica import *
from ecdif import *

def df(y,t):
    df= t**2-y
    return df

y0=0.5
h=0.01
intervalo=[0,5]
sol,t=euler(df,h,intervalo,y0)


grafvector(t,sol,"y'=t^2-y")
titulos("y'=t^2-y","t","y(t)")
muestra()
