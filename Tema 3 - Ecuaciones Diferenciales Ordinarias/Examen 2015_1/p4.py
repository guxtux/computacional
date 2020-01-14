# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:56:43 2014

@author: Abraham
"""

#problema 4
import matplotlib.pyplot as plt
from imprimeSoln import*
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((2),dtype='float64')
    F[0]=y[1]
    F[1]=9.80665*(1-16.0*y[0]**3)
    return F
x=0.0
xAlto=10.0
y=np.array([0.1,0.0])
h=0.001
freq=100
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(X,Y[:,0], 'r-',label='posicion ')
plt.title('posicion v/s tiempo')
plt.xlabel('tiempo')
plt.ylabel('posicion')
plt.legend(loc=1)
plt.subplot(212)
plt.title('diagrama fase')
plt.plot(Y[:,0],Y[:,1], 'c-')
plt.xlabel('posicion')
plt.ylabel('momento')
plt.figure(2)
plt.plot(X,Y[:,0], 'r-',label='posicion ')
plt.title('posicion v/s tiempo')
plt.xlabel('tiempo')
plt.ylabel('posicion')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.75)
plt.text(3,0.5,r'$\tau=0.818$ segundos, $A=0.24623$ m',bbox=props, size=14)
#plt.legend(loc=1)
plt.show()
i=1
#revisamos el periodo considerenado que el punto de retorno, es decir la primera parte 
#del periodo, asi el preriodo completo es dos veces ese punto pero el maximo se
# en ese punto menos las posición inicial para que sea desplazamiento
t=Y[1,1]
while t>0:
    i=i+1
    t=Y[i,1]
#por otra parte analizando los datos podemos ver que el perdo es 0.82seg y la amplitud maxima   
#podemos analizarla de la misma manera tomando la diferencia entre el punto 
#maximo y el punto de inicio y tomado la mitad ya que ese término es 2A
#opservamos que el sistema es conservativo y no disipa dado qe el plano fase que se obtiene da una orbita cerrada
#semejante a la de un oscilador armónico, sumamos un uno para poder tener la condición de igualdad 
print 'el periodo es',X[2*(i+1)],'segundos y la amplitud es',(Y[i+1,0]-0.1)*0.5,'metros'  