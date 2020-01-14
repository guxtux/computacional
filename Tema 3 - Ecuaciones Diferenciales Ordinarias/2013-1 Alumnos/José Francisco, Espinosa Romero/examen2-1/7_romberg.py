# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:12:13 2012

@author: pako
"""

from scipy import *
from scipy.integrate import romberg

def h(x0): 
    def f(x): return 1/sqrt(1.-(sin(x0/2.)**2)*sin(x))
    return f

a=[15,30,45]

print "El valor de h(0°) es:",pi/2.
for i in range(3):
    I=romberg (h(a[i]*pi/180),0,pi/2.)
    e=abs((pi/2.-I)*100/(pi/2.))
    print "\nEl valor de h(",a[i],"° ) es:",I
    print "El error en la integral es:",e,"%"
    
"""
Aquí se utilizó directamente la libreria scipy
para calcular la integral con el metodo romberg
lo cual hizo el problema más sencillo

Para los 2 primeros valores la integral se acerca mucho al valor deseado
sin embargo, para 45° el valor ya tiene un error más grande,
eso nos da una idea de que efectivamente
la aproximación solo sirve para oscilaciones pequeñas
"""
