from ruku3 import *
from grafica import *

h=1
def f(x,t):
    F=[]
    F.append(h*(-(2./50.)*x[0]))
    F.append(h*(-(3./20.)*x[1]+(2./20.)*x[0]))
    return F

y0=[10,0]
concentracion,t=rk2(f,y0,90,h)

T1=[]#tanque 1 50 gal
T2=[]#tanque 2 20 gal
maxi=0
i=0
for a in concentracion:
    T1.append(a[0])
    T2.append(a[1])
    if maxi<a[1]:
        maxi=a[1]
        k=i
    i=i+1
    

grafvector(t,T2,"Tanque 20 Gal")
grafvector(t,T1,"Tanque 50 Gal")
grafpto(t[k],maxi,"maxima en t=(%2.0f) concentracion(%2.2f)"%(t[k],maxi))
titulos("Concentracion en Tanque","tiempo (min)","concentracion (oz/gal)")
muestra()


