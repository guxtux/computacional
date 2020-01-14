# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
RESOLUCIÓN DE UN CIRCUITO USANDO RK2
"""
from math import *
from ecdif import *

def dI(I,t): return V/L-R/L*I
L,R,V=50.,20.,10.
I0,t0,tn=0.,0.,10.
h=0.1
Idatos=rk(2,dI,I0,t0,tn,h,1,1,"t","I(t)","Circuito electrico")
