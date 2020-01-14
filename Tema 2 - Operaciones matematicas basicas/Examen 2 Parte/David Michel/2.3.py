# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:47:02 2013

@author: Deivid
"""
# no supe como trabajaro composicion de funciones, lo unico que se me puede ocurrir es ingresar la fincion ya trabajada con el metodo de simpson13
# y aplicarle a la uncion resultante el metodo de la secante, solo que ya no me dio tiempo
from math import *
from todo import*
def a(En): return ((2-(2*(1+En)**.5))/(1-1+En))**(1/6)
def b(En): return((2+(2*(1+En)**.5))/(1-1+En))**(1/6)
n=8
def f(x): return (En-4*(((1/x)**12)-((1/x)**6)))**1/2-pi*(0+1/2)


print secante(-1.,0.,n,e**-4.,simpson13(f,a,b,n))