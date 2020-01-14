# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:53:06 2013

@author: acesimbrote
"""

from numpy import *

n=8

x= array([0.,1.525,3.050,4.575,6.10,7.625,9.150,9.4,9.8,10.2])
x0= array([10.5])
f=[1.0,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741,0.362981094013,0.345816994912,0.329466008794] 

for k in x0:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i]
    print 'el polinomio evaluado en P(',k,')=',yres 


#Si procedemos directamente a extrapolar el valor en x=10.5, 
#encontramos  P( 10.5 )= 0.317776110522
#Podemos hacer una mejor aproximación si extrapolamos primero
#algunos valores cercanos al último valor, x = 9.150 
#Así, en P(9.4)= 0.362981094013, P( 9.8 )= 0.345816994912, 
#P( 10.2 )= 0.329466008794. Con este procedimiento encuentro 
#P( 10.5 )= 0.317776110525, que es esencialmente lo ya encontrado.                
#
#
#
