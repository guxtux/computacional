# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:39:58 2013

@author: acesimbrote
"""

##module integracion

from numpy import zeros
from math import *

# método del trapecio

def trapecio(f,a,b,Iv,k):
    if k==1: In=(f(a)+f(b))*(b-a)/2.0
    else:
        n = 2**(k-2)
        h = (b-a)/n
        x = a +h/2.0
        suma=0.0
        for i in range(n):
            suma=suma+f(x)
            x=x+h
        In= (Iv + h*suma)/2.0
    return In
    
#Trapecios 2

def trapecios(f,a,b,n):
    h=(b-a)/float(n)
    x=a
    suma=0
    for i in range(1,n):
        x=x+h
        suma = suma + f(x)
    return (h/2.)*(f(a)+f(b)+2*suma)

#Integral simpson  
    
def integralsimpson (f,a,b,xm):
    I=(b-a)*(f(a)+4*f(xm)+f(b))/6
    return I

#Integral simpson 2
    
def Sim13(f,a,b,n):
    n=n-n%2
    if n<=0:
        n=1
    h=(b-a)/n
    x=a
    suma=0
    for j in range(n/2):
        suma += f(x)+4*f(x+h)+f(x+2*h)
        x +=2*h
    return (h/3.)*suma
#
##Romberg
#
#def Romberg(f,a,b,tol=1.0e-6):
#    def richardson(r,k):
#        for j in range(k-1,0,-1):
#            const=4.0**(k-j)
#            r[j]=(const*r[j+1]-r[j])/(const-1.0)
#        return r
#    r=zeros(21)
#    r[1]=trapecio(f,a,b,0.0,1)
#    r_viejo=r[1]
#    for j in range(2,21):
#        r[k]=trapecio(f,a,b,r[k-1],k)
#        r=richardson(r,k)
#        if abs(r[1]-r_viejo)<tol*max(abs(r[1]),1.0):
#            return r[1],2**(k-1)
#            r_viejo=r[1]
#    print 'La integral de ROmberg no converge'
#    

            

