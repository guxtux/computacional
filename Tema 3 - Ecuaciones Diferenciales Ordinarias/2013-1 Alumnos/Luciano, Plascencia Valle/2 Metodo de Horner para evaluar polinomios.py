# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:39:27 2012
@author: Luciano Plascencia Valle
"""
print "Método de Horner para evaluar el polinomio"
print "P(x)=2+4x-5x²+2x³-6x⁴+8x⁵+10x⁶"
print "en x= -1.5, -0.65, 0.1, 1.4, 2.87 \n"

archivo=open("2 Polinomio.dat","w")
x=[-1.5, -0.65, 0.1, 1.4, 2.87]         # Valores de x para evaluar P(x)
a=[2,4,-5,2,-6,8,10]                    # Coeficientes de P(x)

for i in range(len(x)):                 # Bucle para evaluar cada valor de x
    P=0
    for n in range(len(a)-1,-1,-1):     # Bucle del método de Horner
        P=a[n]+P*x[i]
    print "P(%.2f) = %f" %(x[i],P)
    archivo.write("%.10f %.10f \n" %(x[i],P))
archivo.close