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
    while f[i]>0:

        v0=v0+h*vfun(y0,v0,t[i])
        v.append(v0)
        
        y0=y0+h*yfun(v0,y0,t[i])
        f.append(y0)
        
        t.append(t[i]+h)
        i=i+1
    return f,t,v
    
    
