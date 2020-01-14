# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr  4 19:05:41 2013
MÓDULO DE INTEGRACIÓN NUMÉRICA
"""
##module integral
from numpy import zeros
from varios import *
    
def simpson1_3(f,a,b): return (f(a)+4*f((a+b)/2)+f(b))*(b-a)/6
def simpson3_8(f,a,b): return (f(a)+3*f((a+(b-a)/3))+3*f((a+(b-a)*2/3))+f(b))*(b-a)/8
def simpson(f,a,b,n):   #Generaliza el método de Simpson
    h=(b-a)/n           #para todo número entero n de bloques.
    x1=a
    n0=0    
    S=0.
    if n==1:    #Si n=1, calcula usando Trapecio y sale.
        S=S+trapecio(f,x1,x1+h,1)
        return S
    if n%2==1:  #Si n es impar, calcula los 3 primeros bloques
        S=S+simpson3_8(f,x1,x1+3*h)     #usando Simpson 3/8.
        x1=x1+3*h
        n0=3
    for j in range((n-n0)/2):   #Queda un número par de bloques;
        S=S+simpson1_3(f,x1,x1+2*h)     #usamos Simpson 1/3.
        x1=x1+2*h
    return S

def trapecio0(f,a,b,K=1):  #El número de trapecios es n=2**(K-1)
    H=b-a
    I=[0]
    I.append((f(a)+f(b))*H/2)
    for k in range(2,K):  #k dobla el Nº de trapecios hasta llegar a K
        S=0
        for i in range(1,2**(k-2)+1):
            S=S+f(a+(2*i-1)*H/2**(k-1))
        I.append(I[k-1]/2+S*H/2**(k-1))
    return I

def trapecio(f,a,b,k=1,Ivieja=0.):
    if k==1: Inueva=(f(a)+f(b))*(b-a)/2.
    else:
        n=2**(k-2)
        h=(b-a)/n
        x=a+h/2.
        sum=0.
        for i in range(n):
            sum=sum+f(x)
            x=x+h
        Inueva=(Ivieja+h*sum)/2.
    return Inueva
    
def romberg(f,a,b,tol=1e-6):
    def richardson(r,k):
        for j in range(k-1,0,-1):
            const=4.**(k-j)
            r[j]=(const*r[j+1]-r[j])/(const-1.)
        return r
    r=zeros(21)
    r[1]=trapecio(f,a,b,1)
    r_viejo=r[1]
    for k in range(2,21):
        r[k]=trapecio(f,a,b,k,r[k-1])
        r=richardson(r,k)
        if abs(r[1]-r_viejo) < tol*max(abs(r[1]),1.):
            return r[1],2**(k-1)
        r_viejo=r[1]
    print "La integración de Romberg no converge."
