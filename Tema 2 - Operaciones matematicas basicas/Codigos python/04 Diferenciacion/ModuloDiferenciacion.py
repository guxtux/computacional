# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:42:41 2020

@author: gusto
"""

def derivada_dif_central(f, x, h):
    valor = (f(x + h) - f(x - h))/(2*h)
    return valor
    
def seg_derivada_dif_central(f, x, h):
    valor = (f(x + h) - 2*f(x) + f(x - h))/(h**2)
    return valor

def derivada_dif_adelante(f, x, h):
    valor = (f(x + h) - f(x))/h
    return valor

def derivada_dif_atras(f, x, h):
    valor = (f(x) - f(x + h))/h
    return valor

def seg_aprox_derivada_dif_adelante(f, x, h):
    valor = (-f(x + (2*h)) + 4*f(x + h) - 3*f(x))/(2*h)
    return valor