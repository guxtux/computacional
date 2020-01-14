# module ruku3
from numpy import *

def rk2(f,x,tmax,h):
    y=[]
    t=[]
    y.append(x)
    t.append(0)
    i=0
    ptos=int(tmax/h)
    for i in range(ptos):
        F1=f(y[i],t[i])
        F2=f(y[i]+F1,t[i]+h)
        r=[]
        r.append(y[i][0]+.5*(F1[0]+F2[0]))
        r.append(y[i][1]+.5*(F1[1]+F2[1]))
        y.append(r)
        t.append(t[i]+h)
        #i=i+1
    return y,t

def rk3(f,x,tmax,h):
    y=[]
    t=[]
    y.append(x)
    t.append(0)
    i=0
    for i in range(1000):
        F1=f(y[i],t[i])
        F2=f(y[i]+multiply(F1,[.5,.5]),t[i]+h)
        F3=f(y[i]+multiply(F2,[2,2])-F1,t[i]+h)

        r=[]
        r.append(y[i][0]+(1./6.)*(F1[0]+4*F2[0]+F3[0]))
        r.append(y[i][1]+(1./6.)*(F1[1]+4*F2[1]+F3[1]))
        y.append(r)
        t.append(t[i]+h)
        #i=i+1
    return y,t


def rk4(f,x,tmax,h):
    y=[]
    t=[]
    y.append(x)
    t.append(0)
    ptos=int(tmax/h)
    for i in range(ptos):
        F1=f(y[i],t[i])
        F2=f(y[i]+multiply(F1,[(1./3.),(1./3.)]),t[i]+h/3)
        F3=f(y[i]+multiply(F1,[(1./3.),(1./3.)])+multiply(F2,[(1./3.),(1./3.)]),t[i]+2.*h/3.)
        F2a=multiply(F2,[(-1.),(-1.)])
        F4=f(y[i]+F1+F2+F3,t[i]+h)
        
        r=[]
        r.append(y[i][0]+(1./8.)*(F1[0]+3*F2[0]+3*F3[0]+F4[0]))
        r.append(y[i][1]+(1./8.)*(F1[1]+3*F2[1]+3*F3[1]+F4[1]))
        y.append(r)
        t.append(t[i]+h)
        #i=i+1
    return y,t

