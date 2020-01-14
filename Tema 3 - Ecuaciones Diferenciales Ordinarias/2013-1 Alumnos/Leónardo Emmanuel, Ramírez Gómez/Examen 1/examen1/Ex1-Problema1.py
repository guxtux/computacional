# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 02:36:47 2012

@author: emmanuel
"""

from math import*

x=[0.1,1.,10.,100.,1000.]
i=0
while i<=4:
    n=0
    a=0.
    b=1
    y=(-1.)*x[i]
    c=exp(y)
#ciclo para el error
    while b>(10**-8):
        a=a+(y**n)/(factorial(n))
        n=n+1
        b=abs(c-a)/c
    print '-x','-','exp','-','exp program','-','error absoluto'
    print y,'--',c,'--',a,'--',b
    i=i+1
    
#me marca fuera del rango, me imagino que es un numero muy grande, y no estoy
#seguro de como corregir este error, para 100 y 1000
#para obtener el valor de exp de -100 se puede poner print antes del error, pero
#para el error de este ya marca OverFlowError