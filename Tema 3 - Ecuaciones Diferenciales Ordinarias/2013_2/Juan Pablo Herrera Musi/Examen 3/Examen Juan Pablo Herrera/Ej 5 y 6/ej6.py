from ecdif import *
from grafica import *

def f(x,y,t):
    lamda=.1044
    return -lamda*y

def g(x,y,t):
    lamda=.0753
    return lamda*x
N0=1e5
Nx=0
intervalo=[0,50]
h=0.05

n,t,v=euler(f,g,h,intervalo,N0,Nx)

grafvector(t,n,"Ni(t) -->Densidad Yodo")
grafvector(t,v,"Nx(t) -->Densidad Xenon")
titulos("Densidad del yodo->xenon-135","tiempo(hr)","Densidad(atm/cm^3)")

muestra()

