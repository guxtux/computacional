# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:26:08 2013

@author: san
"""
import Gnuplot
from numpy import array

from neville import *
xDatos = array([-1.2,0.3,1.1])
yDatos = array([-5.76,-5.61,-3.69])
print """ El resultado de la interpolación de neville en
los puntos 
x=[-1.2,0.3,1.1]
y=[-5.76,-5.61,-3.69]
con x=0 es %.4f
"""% neville(xDatos,yDatos,0)
n=neville(xDatos,yDatos,0)
x = array([-1.2,0.0,0.3,1.1,])
y = array([-5.76,n,-5.61,-3.69])
g=Gnuplot.Gnuplot(persist=1)
d=Gnuplot.Data(x,y,with_="lines",title="examen2_1a")
g.plot(d)