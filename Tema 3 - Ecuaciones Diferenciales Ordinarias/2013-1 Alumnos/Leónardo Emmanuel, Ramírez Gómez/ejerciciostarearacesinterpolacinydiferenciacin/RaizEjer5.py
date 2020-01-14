# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 02:19:05 2012

@author: emmanuel
"""

#La energia libre de Gibbs en un mol de hidrogeno a una temperatura T es:

   #G=-R*T*log((T/To)**(5/2))------(1)

#donde la constante del gas es:
R=8.311441 #J/K
To=4.44418 #K

#Calcula la temperatura en la cual
G=-10**5 #J


#Despejando (1) para igualar a cero

   #-R*T*log((T/To)**(5/2))-G=0
   
from math import*
def f(T): return R*T*log((T/To)**(5/2))+G

def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2

#El polinomio se indetermina para valores<800 tomamos el intervalo (800,1200)
#ya que para T>1200 el polinomio ya no tiene más raices (se observo esto al
#graficar en gnuplot)
a,b,dx=(800,1200,0.0001)
while a<b:
    print 'El intervalo es:'
    x1,x2=buscaraiz(f,a,b,dx)
    print '(',x1,',',x2,')'
    xmed=(x1+x2)/2.
    print 'la temperatura a la cual G=-10⁵J'
    print xmed,'K'
    print '---------------------'
    a=x2
#EL PROGRAMA TARDA 15 SEG EN DAR RESULTADO