# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Mar 19 20:04:01 2013
MÓDULO DE DIFERENCIACIÓN NUMÉRICA
"""
##module derivada
from math import *
from varios import *

def df_datos(orden,xDatos,yDatos,h,Oh=2):
#Devuelve el valor de la derivada en todos los puntos (xDatos,yDatos)
    def f(x): return evalf(xDatos,yDatos,x,h)
    dec=decimales(h**Oh)
    df=[]
    df.append(round(df_adelante(orden,f,xDatos[0],h,Oh),dec))
    for i in range(1,len(xDatos)-1):
        df.append(round(df_central(orden,f,xDatos[i],h,Oh),dec))
    df.append(round(df_atras(orden,f,xDatos[-1],h,Oh),dec))
    return df
    
def df_central(orden,f,x,h,Oh=2):    
    if orden==1:
        if   Oh==1: df=(f(x+h)-f(x))/h
        elif Oh==2: df=(f(x+h)-f(x-h))/(2*h)
        elif Oh==4: df=(-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
    elif orden==2:
        if   Oh==1: df=(f(x+2*h)-2*f(x+h)+f(x))/h**2
        elif Oh==2: df=(f(x+h)-2*f(x)+f(x-h))/h**2
        elif Oh==4: df=(-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h**2)
    elif orden==3:
        if   Oh==2: df=(f(x+2*h)-2*f(x+h)+2*f(x-h)-f(x-2*h))/(2*h**3)
        elif Oh==4: df=(-f(x+3*h)+8*f(x+2*h)-13*f(x+h)+13*f(x-h)-8*f(x-2*h)+f(x-3*h))/(8*h**3)
    elif orden==4:
        if   Oh==2: df=(f(x+2*h)-4*f(x+h)+6*f(x)-4*f(x-h)+f(x-2*h))/h**4
        elif Oh==4: df=(-f(x+3*h)+12*f(x+2*h)-39*f(x+h)+56*f(x)-39*f(x-h)+12*f(x-2*h)-f(x-3*h))/(6*h**4)
    return df
    
def df_adelante(orden,f,x,h,Oh=2):
    if orden==1:
        if   Oh==1: df=(f(x+h)-f(x))/h
        elif Oh==2: df=(-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h)
        elif Oh==4: df=(-25*f(x)+48*f(x+h)-36*f(x+2*h)+16*f(x+3*h)-3*f(x+4*h))/(12*h)
    elif orden==2:
        if   Oh==1: df=(f(x)-2*f(x+h)+f(x+2*h))/h**2
        elif Oh==2: df=(2*f(x)-5*f(x+h)+4*f(x+2*h)-f(x+3*h))/h**2
    elif orden==3:    
        if   Oh==1: df=(-f(x)+3*f(x+h)-3*f(x+2*h)+f(x+3*h))/h**3
        elif Oh==2: df=(-5*f(x)+18*f(x+h)-24*f(x+2*h)+14*f(x+3*h)-3*f(x+4*h))/(2*h**3)
    elif orden==4:
        if   Oh==1: df=(f(x)-4*f(x+h)+6*f(x+2*h)-4*f(x+3*h)+f(x+4*h))/h**4
        elif Oh==2: df=(3*f(x)-14*f(x+h)+26*f(x+2*h)-24*f(x+3*h)+11*f(x+4*h)-2*f(x+5*h))/h**4
    return df
    
def df_atras(orden,f,x,h,Oh=2): return df_adelante(orden,f,x,-h,Oh)

def richardson(g,h,p=2): return (2**p*g(h)-g(2*h))/(2**p-1)
#OJO: h=hmín, de modo que h1=2*h, h2=h1/2=h
