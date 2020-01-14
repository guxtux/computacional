# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 00:11:02 2013

@author: IIFCES
"""
from numpy import *

def integra(F,x,y,xAlto,h):
    
    def rk_4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3) / 6.0
    
    X = []
    Y = []
    X.append(x)
    Y.append(y)

    while x < xAlto:
        h = min(h, xAlto - x)
        y = y + rk_4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    
    return array(X), array(Y)