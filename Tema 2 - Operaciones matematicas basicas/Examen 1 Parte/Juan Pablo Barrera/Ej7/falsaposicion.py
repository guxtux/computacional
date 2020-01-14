## module falsaposicion
from numpy import *

def buscaraiz (f,a,b,dx):
    x1=a
    f1=f(a)
    x2=a+dx
    f2=f(x2)
    while f1*f2>0.0:
        if x1>=b:
            return 0,0
        x1=x2
        f1=f2
        x2=x1+dx
        f2=f(x2)
    else:
        return x1,x2

def falsaposicion (f,a,c,n):
    #funcion, a,b intevalo
    
    fa=f(a)
    fc=f(c)
    b=(a*fc-c*fa)/(fc-fa)
    i=0
    aa=0
    cc=0
    
    for i in range(n):
    
        b=((a*fc)-(c*fa))/(fc-fa)
        fb=f(b)
        if fb==0:
            return b
        #checa en que intervalo esta la raiz
        #reasinga los limites del intervalo
        if fa*fb<0:
            c=b
            fc=f(b)
            aa=aa+1 #contador de cuantas veces se ha movido a
        if fb*fc<0:
            a=b
            fa=f(a)
            cc=cc+1 #contador de cuantas veces se ha movido c

        #falsa posicion modificada
        if i%2==0:
            if aa==2:
                fa=fa/2
                aa=0
            if cc==2:
                fc=fc/2
                cc=0
            aa=0;cc=0
    return b
