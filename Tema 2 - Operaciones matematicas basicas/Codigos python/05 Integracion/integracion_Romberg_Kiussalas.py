# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:40:07 2020

@author: gusto
"""
import numpy as np

def trapezoid(f,a,b,Iold,k):
    if k == 1:Inew = (f(a) + f(b))*(b - a)/2.0
    else:
        n = 2**(k -2 ) # Number of new points
        h = (b - a)/n # Spacing of new points
        x = a + h/2.0
        sum = 0.0
        for i in range(n):
            sum = sum + f(x)
            x = x + h
        Inew = (Iold + h*sum)/2.0
    
    return Inew

def trapecios(f, x0, xf, n):
   # Se obtiene la integral numerica de la funcion f, desde el valor 
   # inicial x0 al valor final xf mediante el metodo de trapecios, utilizando
   # n+1 datos.
   h = (xf-x0)/n
   x = x0
   suma = 0
   for i in range(1,n):
      x +=h
      suma += f(x)
   return (h/2.)*(f(x0) + f(xf) + 2*suma)

def romberg(f,a,b,tol=1.0e-6):
    def richardson(r,k):
        for j in range(k-1,0,-1):
            const = 4.0**(k-j)
            r[j] = (const*r[j+1] - r[j])/(const - 1.0)
        return r
    
    r = np.zeros(21)
    r[1] = trapezoid(f, a, b, 0.0, 1)
    r_old = r[1]
    
    for k in range(2,21):
        r[k] = trapezoid(f, a, b, r[k-1], k)
        r = richardson(r,k)
        if abs(r[1]-r_old) < tol*max(abs(r[1]),1.0):
            return r[1],2**(k-1)
        r_old = r[1]
        
    print("El método de Romberg no converge")

def f(x): return 2.0*(x**2)*np.cos(x**2)

I, n = romberg(f,0,np.sqrt(np.pi))
print("Integral =", I)
print("numEvals =", n)
input("\nPress return to exit")
