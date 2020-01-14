# Motociclista
"""


@author: Calderon Apolinar Marco A.
"""

 
from math import exp, sin, cos, pi
m=250
g=9.81
c=1
A=0.93
p=1.2
v0=67
b=c*A*p/2*m
q=eval(raw_input("dame un angulo"))
t=eval(raw_input("dame un tiempo: "))
o=q*pi/90
e=exp(-b*t)
x=(v0*cos(o)*(1-e))/b
y=((g+b*v0*sin(o)*(1-e)/b)-g*t)/b
print "las coordenadas de un motociclista en "
print "t=%f segundos son x=%f y y=%f " %(t,x,y)
