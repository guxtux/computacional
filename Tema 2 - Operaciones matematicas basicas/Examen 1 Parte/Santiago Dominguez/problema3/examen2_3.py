# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:58:31 2013

@author: san
"""

from numpy import array

from neville import *

xDatos =array([0.0,0.5,1.0,1.5,2.0,2.5,3.0])
yDatos =array([1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727])
print """ El resultado de la interpolación de neville en
los puntos 
x=[-1.2,0.3,1.1]
y=[-5.76,-5.61,-3.69]
para encontrar el valor maximo en x=0.7679 es %.4f
"""% neville(xDatos,yDatos,0.7679)