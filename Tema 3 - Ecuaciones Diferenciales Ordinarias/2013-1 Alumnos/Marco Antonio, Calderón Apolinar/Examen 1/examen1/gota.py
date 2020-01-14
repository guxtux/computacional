# gota de agua
"""
Created on Sat Sep  8 22:31:43 2012

@author: usuario
"""

from math import exp
g=9.81
m=0.1
k=1
v0=0
y0=eval(raw_input("cual es la posicion inicial"))
t=eval(raw_input("a que tiempo quieres conocer la altura"))
y=((m*g+k*v0)*(1-exp((-m*t)/k))/m)-((m*g*t)/k)+y0
print "la altura al tiempo %.2f s es %.3f m" %(t,y)
vt=-m*g/k
print "la velocidad terminal es %.3f m/s" %vt