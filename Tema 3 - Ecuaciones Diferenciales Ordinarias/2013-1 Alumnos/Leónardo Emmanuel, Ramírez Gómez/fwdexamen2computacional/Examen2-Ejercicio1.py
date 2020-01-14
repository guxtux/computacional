# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:51:31 2012

@author: emmanuel
"""


"""
La trayectoria de un satélite que orbita la Tierra es: 
    R=C/(1+e*sin(t+a))
donde (R,t) son las coordenadas polares del satélite, C, e y a son
constantes (e se conoce como la excentricidad de la órbita).
Si el satélite fue observado en las siguientes tres posiciones: 
    t       -30°    0°      30°
    R(km)   6870    6728    6615
Determina el valor más pequeño de R en la trayectoria y el respectivo valor
de t.
"""


#Usando una interpolacion cuadratica encontramos el polinomio que describe
#la trayectoria



a=(6870./1800.)-(6728./900.)+(6615./1800.)
b=-114.5+6728.+110.25
c=0.

print 'El polinomio que describe la trayectoria es:'
print 'R(t)=',a,'t²+',b,'t+',c