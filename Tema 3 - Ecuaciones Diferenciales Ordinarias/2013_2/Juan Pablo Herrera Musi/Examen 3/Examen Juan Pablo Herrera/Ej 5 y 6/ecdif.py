##module ecdif
from math import *

def euler(yfun,vfun,h,intervalo,y0,v0):
    f=[]
    f.append(y0)
    v=[]
    v.append(v0)
    t=[]
    t.append(intervalo[0])
    i=0
    while t[i]<=intervalo[1]:

        v0=v0+h*vfun(y0,v0,t[i])
        v.append(v0)
        
        y0=y0+h*yfun(v0,y0,t[i])
        f.append(y0)
        
        t.append(t[i]+h)
        i=i+1
    return f,t,v
    
def eulermod(yfun,vfun,h,intervalo,x0,y0):
    f=[]
    f.append(y0)
    v=[]
    v.append(x0)
    t=[]
    t.append(intervalo[0])
    i=0
    while t[i]<=intervalo[1]:

        v0=v0+h*yfun(y0,v0+(h/2)*vfun(y0,v0,t[i]),t[i])
        v.append(v0)
        
        y0=y0+h*(yfun(v0,y0+(h/2)*yfun(v0,y0,t[i]),t[i]))
        f.append(y0)
        
        t.append(t[i]+h)
        i=i+1
    return f,t,v
