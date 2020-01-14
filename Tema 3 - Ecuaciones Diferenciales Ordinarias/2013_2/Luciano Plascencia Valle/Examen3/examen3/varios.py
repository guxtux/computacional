# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Mon Apr 15 02:12:39 2013
MÓDULO DE FUNCIONES Y UTILERÍAS VARIAS
"""
##module varios
from math import *
import numpy as np
import matplotlib.pyplot as plt

def Eabs(x0,x): return abs(x-x0)
def Erel(x0,x): return abs((x-x0)/x0)

def decimales(h):
    decimales=0
    while int(h)!=h:
        h=h*10
        decimales=decimales+1
    return decimales
    
def orden_magnitud(h):
    h=abs(h)
    orden=0
    if h>=1 and h<10: orden=0
    elif int(h)==0:
        while int(h)==0:
            h=h*10
            orden=orden-1
    elif int(h)>=10:
        while int(h)>=10:
            h=h/10
            orden=orden+1
    return orden

def decformat(h,todos_decimales=0):
    if todos_decimales==0: o=orden_magnitud(h)
    elif todos_decimales==1: o=-decimales(h)
    if o<0: return "%."+str(-o)+"f"
    else: return "%"+str(o+1)+".f"

def evalf(xDatos,yDatos,x,h):   
#Devuelve el valor y=f(x) de parejas de conjuntos xDatos,yDatos.
#Devuelve y=None si x no está en xDatos.
#Para evitar error por redondeo introducimos "dec",
#que es el número de cifras decimales del parámetro h.
    dec=decimales(h)
    indices=range(len(xDatos))
    for i in indices:
        if round(x,dec)==round(xDatos[i],dec): return yDatos[i]

def grafica(f,a,b,h):          #Rutina para graficar f
    xDatos=np.arange(a,b,h)
    plt.plot(xDatos,f(xDatos),"r-")
    plt.grid()
    plt.show()
    return
