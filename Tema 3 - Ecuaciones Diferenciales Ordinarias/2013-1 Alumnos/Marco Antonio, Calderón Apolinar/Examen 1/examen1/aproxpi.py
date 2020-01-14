# Aproximacion a pi
"""
Created on Sun Sep  9 02:19:15 2012

@author: usuario
"""

from math import sqrt, sin, pi

n=eval(raw_input("que aproximacion quieres"))
r=sin(2*pi/2**(n-1))
seno=r/sqrt(2*(1+sqrt(1-r**2)))
p=(2**(n-1))*seno

print "la aproximacion a pi es %f " %p