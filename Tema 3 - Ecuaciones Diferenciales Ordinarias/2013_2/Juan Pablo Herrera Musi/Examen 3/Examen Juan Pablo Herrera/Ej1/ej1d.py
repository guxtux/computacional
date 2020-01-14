from grafica import *
from ecdif import *

def df(y,t):
    df= -y*abs(y)
    return df

y0=1
h=0.01
intervalo=[0,5]
sol,t=euler(df,h,intervalo,y0)


grafvector(t,sol,"y'+y*abs(y)=0")
titulos("y'+y*abs(y)=0","t","y(t)")
muestra()
