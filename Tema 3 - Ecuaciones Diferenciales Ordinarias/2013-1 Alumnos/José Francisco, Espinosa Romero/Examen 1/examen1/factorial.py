# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:33:02 2012

@author: pako
"""

def fact(N):
    i=0
    f=1
    while i<N:
        i=i+1
        f=f*i
    return f
j=0
while j<10:
    print fact(j)
    j+=1