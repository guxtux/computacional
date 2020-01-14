# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 18:37:44 2013
SOLUCIÓN DE EDO CON MÉTODO DE EULER
dy/dt = -20*y + 7*exp(-t/2)
"""
from math import *
from ecdif import *

print "h       tn      y(tn)  yexacta  Err.abs. Err.rel."
for h in [.01,.001,.0001]:
    y=5.
    t=0.
    n=0
    while t<=0.09:
        n=n+1
        y=y+h*(-20.*y+7.*exp(-t/2.))
        t=n*h
        yexacta=5*exp(-20.*t)+(7/19.5)*(exp(-t/2)-exp(-20.*t))
    print "%6.4f  %6.4f  %6.4f  %6.4f   %6.4f   %6.4f" %(h,t,y,yexacta,Eabs(yexacta,y),Erel(yexacta,y))

"""
El código original dado en clase de este programa tiene dos errores:
1. El ciclo while da dos vueltas más para h=.01 y h=.001
2. La yexacta se calcula con t[n].  Por tanto, hay que subir la 
línea de t=n*h arriba del cálculo de yexacta para que ésta se 
calcule con t[n+1] y a la hora de comparar los errores no se haga
entre y(t[n+1]) y yexacta(t[n]).
"""