# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 00:36:32 2013

@author: acesimbrote
"""
##module Euler

from numpy import *
H=[]

def Euler_adelante(f,y,t,n,h):
    for i in range(n):
        yn=f(y,t)
        yn=y+h*yn
        t=t+h
        y=yn
        H.append(y)
    return H

#H=[]
#
#def Euler_adelante(f,y,t,n,h):
#    if h<=n:
#        yn=f(y,t)
#        yn=y+h*yn
#        t=t+h
#        y=yn
#        H.append(y)
#    return H