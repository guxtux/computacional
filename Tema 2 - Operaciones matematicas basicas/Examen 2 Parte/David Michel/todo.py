# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:27:38 2013

@author: Deivid
"""
##module todo

def secante(x0, x1, ite, tol, fx ):
		y0 = eval(fx.replace("x","x0"))
		y1 = eval(fx.replace("x", "x1"))
		error = tol + 1
		cont = 0
		x2 = 0
		while y0 != 0 and error > tol and cont < ite and y1 - y0 != 0:
			x2 = x1 - (y1*(x1-x0)) / (y1-y0)
			y2 = eval(fx.replace("x","x2"))
			print x0,x1, y0, y1, error	        
			error = abs(x2 - x1)
			cont = cont + 1
			x0 = x1
			y0 = y1
			x1 = x2
			y1 = y2
		if y0 == 0:
				print str(x0) + " es raiz"
		else:
				if error < tol:
						print str(x0), " es raiz con un error: ", error, x1, y0, y1
				else:
						if y1 - y0 == 0:
								print "Division por cero"
						else:
								print "No se encontro la raiz"

if __name__=="__main__":
		secante(1,2,20,0.005,"x-2")
  
def error(a,real):
    return abs(real-a)/real
       
def simpson13(f,a,b,n):
    n=n-n%2
    if n<=0:
        n=1
    def h(x): return(b-a)/n
    x=a
    suma=0
    for j in range(n/2):
        suma += f(x)+4*f(x+h)+f(x+2*h)
        x +=2*h
    return (h/3.)*suma

def trapecio1(f,a,b,n):
    h=(b-a)/float(n)
    x=a
    suma=0
    for j in range(1,n):
        x=x+h
        suma = suma + f(x)
    return (h/2.)*(f(a)+f(b)+2*suma)
    
from numpy import zeros
from math import *

def trapecio (f,a,b,Iviejo,k):
    if k==1:
        Inueva=(f(a)+f(b))*(b-a)/2.0
    else:
        n=2**(k-2)
        h=(b-a)/n
        x=a+h/2.0
        sum=0.0
        for i in range(n):
            sum=sum+f(x)
            x=x+h
        Inueva=(Iviejo+h*sum)/2.0
    return Inueva

def romberg(f,a,b,tol=1.0e-6):

    def richardson(r,k):
        for j in range(k-1,0,-1):
            const=4.0**(k-j)
            r[j]=(const*r[j+1]-r[j])/(const-1.0)
        return r

    r=zeros(21)
    r[1]=trapecio(f,a,b,0.0,1)
    r_viejo=r[1]
    
    for k in range(2,21):
        r[k]=trapecio(f,a,b,r[k-1],k)
        r=richardson(r,k)
        if abs(r[1]-r_viejo)<tol*max(abs(r[1]),1.0):
            return r[1],2**(k-1)
        r_viejo=r[1]
    print("la integracion romberg no converge")
    
