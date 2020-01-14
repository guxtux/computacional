#module ecdif
from math import *

def euler(df,h,intervalo,y0):
    y=y0
    sol=[]
    t=[]
    sol.append(y0)
    t.append(intervalo[0])
    i=0
    while t[i]<=intervalo[1]:
        y=y+h*df(y,t[i])
        sol.append(y)
        t.append(t[i]+h)
        i=i+1
    return sol,t
    
    
