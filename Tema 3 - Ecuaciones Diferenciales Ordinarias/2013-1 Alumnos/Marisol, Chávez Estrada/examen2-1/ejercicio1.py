# -*- coding: utf-8 -*-
"""
PROBLEMA 1
"""
from math import *
from numpy import *
import numpy as np
theta=0.0

def dr(theta): return (141.7395*cos(theta+np.radians(8.98)))/((1+0.021*(np.sin(theta+np.radians(8.98))))**2)
def r(theta): return 6749.5/(1+0.021*sin(theta+np.radians(8.98)))

ch=np.array([0.0,0.0])
ra=np.zeros([3600001])
dra=np.zeros([3600001])
dra[0]=dr(0)

for n in range(0,1200000):    				 
	theta= (0.000005+0.000005*n)				 
	ra[n+1]=dr(theta)				 
	if ra[n+1]>0 and ra[n+1]<0.0005 :
		
		print"dr ",ra[n+1],theta,r(theta)	

print "El maximo es el mayor "	

