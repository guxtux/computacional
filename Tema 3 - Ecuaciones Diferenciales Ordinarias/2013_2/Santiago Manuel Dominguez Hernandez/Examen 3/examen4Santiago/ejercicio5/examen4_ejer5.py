# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:28:11 2013

@author: san
"""


from matplotlib.pylab import*    
from math import*
import  numpy as np

#La densidad númerica (número de átomos por cm^3)
#del yodo-135 (radioisótopo) satisface la ecuación 
# d/dtN_i(t)=-LamN_i(t)
#donde N_i es la densidad númerico del yodo-135 y Lam_i es su constante
#de deacaimiento, igual a 0.1044 horas^-1 .
#Si N_1(0).
h=0.05
t=np.linspace(0,1,50)
x=np.linspace(0,1,50)
def f(x,t):
    return 0.1044*x
xn=np.zeros(50)
for n in range(49):
    xn[0]=10e5
    t[n]=n*h
    xn[n+1]=xn[n]+h*f(xn[n],t[n])
print xn 
plot(t,xn)
show()   
