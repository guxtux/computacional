# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 18:20:00 2014

@author: Abraham
"""

#funcion integra con RK4
import numpy as np
def integra(F,x,y,xAlto,h):
    
    def rk_4(F,x,y,h):
        K0=h*F(x,y)
        K1=h*F(x+h/2.0,y+K0/2.0)
        K2=h*F(x+h/2.0,y+K1/2.0)
        K3=h*F(x+h,y+K2)
        return (K0+2.0*K1+2.0*K2+K3)/6.0
        
    X=[]
    Y=[]
    X.append(x)
    Y.append(y)
    
    while x<xAlto:
        h=min(h,xAlto-x)
        y=y+rk_4(F,x,y,h)
        x=x+h
        X.append(x)
        Y.append(y)
        
    return np.array(X), np.array(Y)
