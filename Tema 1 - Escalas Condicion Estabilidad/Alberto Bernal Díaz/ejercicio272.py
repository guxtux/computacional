# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:59:51 2013

@author: est5
"""

import matplotlib.pyplot as plt
import numpy as np
import cmath
n=1.0
j=1.0
k=1.0
s1=0.0
s2=0.0
s3=0.0
N=input("escribe el valor de N (con N entero >0): ")
while n<=2*N:
    s1=s1+((((-1)**n)*n)/(n+1))
    n=n+1
while j<=N:
    s2=s2+(-(((2*j)-1)/(2*j))+((2*j)/((2*j)+1)))
    j=j+1
while k<=N:
    s3=s3+(1/((2*k)*((2*k)+1)))
    k=k+1
print " S1 = ", s1
print " S1 = ", s2
print " S1 = ", s3

"me falta graficar"