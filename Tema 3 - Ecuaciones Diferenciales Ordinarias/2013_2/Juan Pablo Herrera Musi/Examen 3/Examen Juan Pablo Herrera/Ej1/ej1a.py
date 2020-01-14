
from ecdif import *

from grafica import *

def df(y,t):
    df=1-y*t
    return df


y0=1
h=0.01
intervalo=[0,5]
sol,t=euler(df,h,intervalo,y0)

grafvector(t,sol,"dy'+ty=1")
titulos("dy'+ty=1","t","y(t)")
muestra()


