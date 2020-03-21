# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Mar 12 18:51:06 2013
MÓDULO PARA CÁLCULO DE RAÍCES
"""
##module raices
from math import *
import numpy as np
import matplotlib.pyplot as plt

"""La función toda_raiz encuentra todas las raíces de la función f
    en el intervalo (a,b).  
Puede imprimir las raíces con prn=1
    y puede imprimir los intervalos con prn=2
Puede graficar las raíces con plot=1
Puede usar varios métodos para calcularlas:
    0=bisect
    1=newton_raphson (Si se usa éste hay que dar el valor de la
        función derivada df)
    2=secante
"""
def toda_raiz(f,a,b,dx,epsilon=1e-9,prn=0,plot=0,metodo=0,df=0):
    raiz=[]
    x1=a
    k=1
    k_no_sing=1
    while x1<b:
        if intervalo_raiz(f,x1,b,dx)==None: 
            if plot==1: grafica(f,a,b,dx)
            return None    
        x1,x2=intervalo_raiz(f,x1,b,dx)
        if   metodo==0: xraiz=bisect(f,x1,x2,0,epsilon)
        elif metodo==1: xraiz=newton_raphson(f,df,x1,x2,epsilon)
        elif metodo==2: xraiz=secante(f,x1,x2,epsilon)
        if xraiz!=None: raiz.append(xraiz)
        decimales="%."+str(abs(int(round(log(epsilon)/log(10)))))+"f"
        decimales_intervalo="\nLa raíz en el intervalo ("+decimales+","+decimales+") es:"
        if prn==2: print decimales_intervalo %(x1,x2)
        if prn>=1: print "x",k_no_sing,"=",decimales %raiz[k-1]
        if plot==1: plt.plot(xraiz,0,"bo")   
        k_no_sing=k_no_sing+1
        k=k+1
        x1=x2
    #else: return raiz
    #if plot==1: plt.show()
    return raiz
    
def grafica(f,a,b,dx):          #Rutina para graficar f
    xdominio=np.arange(a,b,dx)
    yrango=[]
    for i in xdominio:
        yrango.append(f(i))
    plt.plot(xdominio,yrango,"r-")
    plt.grid()
    plt.show()
    return
   
def intervalo_raiz(f,a,b,dx):
    x1=a; f1=f(x1)
    x2=a+dx; f2=f(x2)
    while f1*f2>0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else: return x1,x2

def bisect(f,x1,x2,switch=1,epsilon=1e-9):
    f1=f(x1)
    if f1==0.: return x1
    f2=f(x2)
    if f2==0.: return x2
    
    if f1*f2>0: print "La raíz no está en el intervalo."
    n=ceil(log(abs(x2-x1)/epsilon)/log(2.))
    
    for i in np.arange(n):
        x3=(x1+x2)/2.;f3=f(x3)
        if (switch==1) and (abs(f3)>abs(f1)) and (abs(f3)>abs(f2)):
            return None     #Esto es para evitar evaluar singularidades
        if f3==0.: return x3
        if f2*f3<0.:
            x1=x3;f1=f3
        else:
            x2=x3;f2=f3
    return (x1+x2)/2.

def newton_raphson(f,df,a,b,epsilon=1e-9):
    fa=f(a)
    if fa==0.: return a
    fb=f(b)
    if fb==0.: return b
    if fa*fb>0.: print "La raíz no está en el intervalo"
    x=(a+b)/2
        
    for i in range(30):
        fx=f(x)
        if abs(fx)<epsilon: return x
        if fa*fb<0.: b=x
        else: a=x;fa=fx
    
        dfx=df(x)
        
        try: dx=-fx/dfx
        except ZeroDivisionError: dx=b-a
        x=x+dx
        
        if(b-x)*(x-a)<0.:
            dx=(b-a)/2
            x=a+dx
        
        if abs(dx)<epsilon*max(abs(b),1.):
            return x

    print "Son demasiadas iteraciones."
        
def secante(f,x0,x1,epsilon=1e-9):
    y2=2*epsilon
    while abs(y2)>epsilon:
        y0=f(x0)
        y1=f(x1)
        x2=x1-y1*(x1-x0)/(y1-y0)
        y2=f(x2)
        x0=x1
        x1=x2
    return x2
