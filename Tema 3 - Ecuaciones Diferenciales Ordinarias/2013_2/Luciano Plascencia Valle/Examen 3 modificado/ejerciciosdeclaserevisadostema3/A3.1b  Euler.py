# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 18:37:44 2013
SOLUCIÓN DE EDO CON MÉTODO DE EULER
dy/dt = -20*y + 7*exp(-t/2)
"""
from math import *
from ecdif import *

def dy(y,t): return -20*y + 7*exp(-t/2)
def yexacta(t): return 5.*exp(-20.*t)+(7/19.5)*(exp(-t/2.)-exp(-20.*t))

y0,t0,tn=5.,0.,0.09
print "h       tn      y(tn)  yexacta  Err.abs. Err.rel."
for h in [.01,.001,.0001]:
    y=rk(1,dy,y0,t0,tn,h)
    ycalc=y[-1]
    print "%6.4f  %6.4f  %6.4f  %6.4f   %6.4f   %6.4f" %(h,tn,ycalc,yexacta(tn),Eabs(yexacta(tn),ycalc),Erel(yexacta(tn),ycalc))
