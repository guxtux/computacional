# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:05:55 2013

@author: acesimbrote
"""

#module ecuaciones diferenciales

from numpy import *


#Euler hacia adelante para primer orden

H=[]

def Euler_adelante(f,y,t,n,h):
    for i in range(n):
        yn=f(y,t)
        yn=y+h*yn
        t=t+h
        y=yn
        H.append(y)
    return H

#Runke-Kutta orden 2 para ecuaciones de segundo orden

S=[]
J=[]

def Run_Kutta2(f,y,z,t,n,h):
    for i in range(n):
        k1=h*f(y,z,t)
        I1=h*g(y,z,t)
        t=t+h
        k2=h*f(y+k1,z+I1,t)
        I2=h*g(y+k1,z+I1,t)
        z=z+(I1+I2)*0.5
        y=y+(k1+k2)*0.5

        S.append(z)
        J.append(y)
    return S,J