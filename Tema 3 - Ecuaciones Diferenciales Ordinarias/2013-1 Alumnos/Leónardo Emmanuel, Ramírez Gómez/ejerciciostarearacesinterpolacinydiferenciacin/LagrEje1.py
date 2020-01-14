# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:43:21 2012

@author: emmanuel
"""

#La densidad del aire p varia con la altura de la siguiente manera:
"""    
    h(km)       0       3       6
    p(kg/m³)    1.225   0.905   0.652
"""    
#Define p(h) como una función cuadrática a partir del método de Lagrange

#Dividimos los 3 terminos x,x²,x³ con sus coeficientes a,b,c; y los calculamos
a=1.225/18.+0.905/-9.+0.652/18.
b=-9.-3.-6.
c=18.
#Obtenidos directamente de la sustitución de los valores en la ec. inter de Lagr

print 'el polinomio es:'
print 'p(h)=',a,'h²+',b,'h+',c