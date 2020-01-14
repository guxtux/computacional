# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:51:32 2014

@author: Abraham
"""

#problema 3
import matplotlib.pyplot as plt
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((2),dtype='float64')
    F[0]=y[1]
    F[1]=(1.0/0.25)*(10*x-75*y[0])
    return F

def G(x,y):
    G=np.zeros((2),dtype='float64')
    G[0]=y[1]
    G[1]=(1.0/0.25)*(20.0-75*y[0])
    return G
x=0.0
xAlto=2.0
x=0.0
xAlto=2.0
#fijamos esa posiscipon incial finalmente se movera respect a un centro y sobre 
#este se pueden ver los desplaxamientos respecto a esa vriable así fijamos nuestro sistema
# de referencia en el punto de equilibrio con lo cual las condiciones inicales
#son 0,0 
y=np.array([0.0,0.0])
h=0.001
X,Y=integra(F,x,y,xAlto,h)
u=len (X) 
x2=2.0
xAlto2=8.0
#para asegurar la continuidad tomamos el inicio de la nueva ecuación con p(t) en los extremos 
#de ambas condiciones  
y2=np.array([Y[u-1,0],Y[u-1,1]])
X2,Y2=integra(G,x2,y2,xAlto2,h)


plt.plot(X,abs(Y[:,0]), 'r-',label='movimiento oscilatorio')
plt.plot(X2,abs(Y2[:,0]), 'r-')
plt.title('deplazamiento v/s tiempo')
plt.text(2,0.10,u'El desplazamiento máximo es 0.28294 metros')
plt.xlabel('tiempo')
plt.ylabel('desplazamiento')
plt.legend(loc="best")
plt.show()

#de la grafica vemos lo siguiente si tenemos la fuerza que actua en el tiempo la
#el desplazamiento va creciendo en forma que cuando el tiempo t es mayor a dos 
#se tiene un oscilador libre así al comienzo del segundo inrvalo tenemos una posición de equiibrio nuevo sobre la 
#cual se mueve asi el desplazamiento maximo es el punto donde se reinicia le mov y de aqui se observa la amplitud del mismo 
# asi la distacia sera xde equlibrio+ ampliitud mediante la drafica se puede analizar los periodos y determinar el valor de esta maximo
#así imprimimos el resultado, escaneado los datos con np.max

print'la distancia de maximo desplazamiento es',np.max(Y2[:,0]),'metros'