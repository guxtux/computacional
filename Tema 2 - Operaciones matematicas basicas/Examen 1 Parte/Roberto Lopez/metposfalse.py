##module metposfalse
from math import *
def metposfalse(f,x1,x2,epsilon=1.0e-9,N=40):
    i=2
    y1=f(x1)
    y2=f(x2)
    while i<= N:
        r=float(x2-(y2*((x2-x1)/(y2-y1))))
        if y1==0:return x1
        if y2==0:return x2
        if abs(r-x2)<= epsilon:return r
        i=i+1
        yr=f(r)
        if yr*y2<0.0:
            x1=x2
            y1=y2
        x2=r
        y2=yr
    print "Demasiadas iteraciones:",i
        
    
