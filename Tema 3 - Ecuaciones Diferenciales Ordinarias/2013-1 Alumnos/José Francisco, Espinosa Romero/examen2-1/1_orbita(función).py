# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:47:08 2012

@author: pako
"""
from math import *
from numpy import *

E=0.04059
A=19.473*pi/180
C=6819.05

def R(t):
    t=t*pi/(180)
    r=C/(1+E*sin(t+A))
    return r

def dR(t):
    t=t*pi/(180)
    r=-C*E*cos(t+A)/(1+E*sin(t+A))**2
    return r

#print R(-30),R(0),R(30)
#print dR(-30),dR(0),dR(30)

def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return b,b
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else: return x1,x2

def bisecta(f,a,b):
    x1=a; f1=f(a)
    x2=b; f2=f(b)
    x3=(a+b)/2.; f3=f(x3)
    if x1==0.0: return x1
    else:
        while abs(x1-x2)>1e-4:
            if f1*f3<0.0: 
                x2=x3; f2=f(x2)
                x3=(x1+x2)/2.; f3=f(x3)
                #print x1,x2
            elif f2*f3<0.0:
                x1=x3; f1=f(x1)
                x3=(x1+x2)/2.; f3=f(x3)
                #print x1,x2
        return x1

print "El valor teórico de las raíces es: ",90-A*180/pi,"y",270-A*180/pi,"\n"

a,b,dx=(0.0,360,10)
raiz=0.0
r=[]
while raiz<b:
    x1,x2=buscaraiz(dR,a,b,dx)
    raiz=bisecta(dR,x1,x2)
    if x1!=x2:
        print 'El intervalo en el que hay una raiz es: (',x1,',',x2,')'
        print 'La raiz es:',raiz
        print "R(",raiz,")=",R(raiz)
        r.append(raiz)
        a=x2
        if a<=b:
            print "\nEl nuevo intervalo es: (",a,",",b,")"
    else: print "No hay más raícez en el intervalo\n"

print "El valor de t para el cual R(t) es mínimo es: %3.5f°" %(r[0])

"""
Los valores de las constantes los determine mediante
un sistema de ecuaciones y una relación trigonométrica
con ello solo tuve que definir la función y su derivada
y obtener las raíces por el método de la bisección
de la derivada para ver los valores críticos,
luego evalue los valores en la función y obtuve el valor mínimo,
que concuerda con el valor teórico
"""