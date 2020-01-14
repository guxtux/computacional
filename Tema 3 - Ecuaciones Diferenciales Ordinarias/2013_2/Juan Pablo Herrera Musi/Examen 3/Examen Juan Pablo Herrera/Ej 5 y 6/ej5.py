from ecdif import *
from grafica import *

def f(x,y,t):
    lamda=.1044
    return -lamda*y

def g(x,y,t):
    return x
N0=1e5
intervalo=[0,50]
h=0.05

n,t,v=euler(f,g,h,intervalo,N0,0)

i=0
while t[i]-1<=0:
    i=i+1

grafvector(t,n,"N(t) -->Densidad ")
titulos("Densidad del yodo-135","tiempo(hr)","Densidad(atm/cm^3)")
grafpto(t[i],n[i],"N(1hr)=%3.0f atm/cm^3"%(n[i]))
muestra()
print("La densidad de atomos en t=1hr es %6.5f"%(n[i]))
