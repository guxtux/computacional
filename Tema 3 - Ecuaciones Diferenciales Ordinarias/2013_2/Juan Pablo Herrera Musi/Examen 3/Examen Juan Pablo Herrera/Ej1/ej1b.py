from grafica import *
from ecdif import *

def df(y,t):
    df= exp(-t)-3*y
    return df

y0=1
h=0.01
intervalo=[0,5]
sol,t=euler(df,h,intervalo,y0)

grafvector(t,sol,"y'+3y=e^(-t)")
titulos("y'+3y=e^(-t)","t","y(t)")
muestra()
