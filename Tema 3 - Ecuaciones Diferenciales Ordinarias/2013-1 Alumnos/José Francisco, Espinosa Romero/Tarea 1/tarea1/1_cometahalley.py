# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 21:33:40 2012

@author: pako
"""

from math import *
g=open('Cometa Halley','w')
s=open('sol','w')
s.write('0.0000000 0.000000')
s.close()

Q=5.28*10**9
G=6.67*10**-20
M=1.99*10**30
k=G*M
V=0.912
e=0.96799
a=Q/(1+e)
r0=a*(1-e*e)
e1=1-(V**2)/k
print "La excentricidad calculada fue:",e1,"y la real:",e
w=0.0
while w<60*pi:
    r=r0/(1+e*cos(w)) 
    print "(w,r)=(",w,"rad,",r,"km)"
    g.write('%f %f\n'%(w,r))
    w=w+pi/3
g.close()
P=2*pi*((a**3)/k)**0.5
P=P/(3600*24*365)
print "El periodo del cometa halley es de:",P,"años"