# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:58:54 2012

@author: emmanuel
"""

import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[48.,100.,70.,-20.,2.]
z=[]
n=4
b=0.
a=-4
dat=open('polinomio.dat','w')
print 'punto','-','valor del polinomio'
while a<=-1:
    while n>=0:
        b=y[n]+a*b
        n=n-1
    x.append(a)
    z.append(b)
    dat.write('%-12f %-12f\n'%(a,b))
    print a,'-',b
    b=0
    a=a+0.5
    n=4
dat.close()
#graficando
plt.figure(1)
plt.subplot(212)
plt.plot(x,z,'bs')
t=np.arange(-4,-1,0.5)
plt.subplot(212)
plt.plot(t,48+100*t+70*t**2-20*t**3+2*t**4,'r--')
plt.xlabel('puntos a evaluar')
plt.ylabel('valor del polinomio')
plt.show()

#se hace una buena aproximación ya que los puntos caen entro de la curva
#del polinomio graficado.