# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:13:50 2020

@author: gusto
"""
from math import fabs

def FalsPos(Func, a, b):
#----------------------------------------------------------------------------
# Determines a real root x of function Func isolated in interval [a,b] by
# the false position method
# Error code: 0 - normal execution
# 1 - [a,b] does not isolate one root or contains several roots
# 2 - max. number of iterations exceeded
#----------------------------------------------------------------------------
    eps = 1e-10 # relative precision of root
    
    itmax = 100 # max. no. of iterations
    
    x = a; fa = Func(x) # is a the root?
    if (fabs(fa) == 0e0): return (x, 0)
    
    x = b; fb = Func(x) # is b the root?
    if (fabs(fb) == 0e0): return (x, 0)
    
    if (fa*fb > 0): return (x, 1) # [a,b] does not contain a root
    # or contains several roots
    
    for it in range(1, itmax+1):
        x = (a*fb - b*fa)/(fb - fa) # new approximation
        fx = Func(x)
        if (fa*fx > 0): # choose new bounding interval
            dx = x - a; a = x; fa = fx
        else:
            dx = b - x; b = x; fb = fx
            
        if ((fabs(dx) <= eps*fabs(x)) or (fabs(fx) <= eps)): return (x,0)
    print("FalsPos: max. no. of iterations exceeded !"); return (x,2)