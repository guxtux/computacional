##module secante
import numpy as np
from math import *
def secante(f,x1,x2,epsilon=1.0e-9,N=40):
    i=2
    y1=f(x1)
    y2=f(x2)
    while i<= N:
        r=x2-(y2*((x2-x1)/(y2-y1)))
        if abs(r-x2)<= epsilon:return r
        i=i+1
        x1=x2
	y1=y2
	x2=r
	y2=f(r)
    print "Demasiadas iteraciones:",i
        
    
