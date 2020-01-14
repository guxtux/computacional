## module bisecccion
from numpy import *

def buscaraiz (f,a,b,dx):
    x1=a
    f1=f(a)
    x2=a+dx
    f2=f(x2)
    while f1*f2>0.0:
        if x1>=b:
            return b+1,b+1
        x1=x2
        f1=f2
        x2=x1+dx
        f2=f(x2)
    else:
        return x1,x2

def bisect (x1,x2,switch,epsilon,f):
    f1=f(x1)
    if f1==0:
        return x1
    f2=f(x2)
    if f2==0:
        return x2
    if f1*f2>0.0:
        print("la raiz no esta en el intervalo")
    n=ceil(log(abs(x2-x1)/epsilon)/log(2.0))
   
    
    for i in arange(n):
        x3=0.5*(x1+x2)
        f3=f(x3)
        if (switch==0) and (abs(f3)>abs(f1)) and (abs(f3)>abs(f2)):
            return None
        if f3==0.0:
            return x3
        if f2*f3<0.0:
            x1=x3
            f1=f3
        else:
            x2=x3
            f2=f3

    return x3
