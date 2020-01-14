# calculo de la serie para exp(-x)
# Este programa solo funciona con valores menores a 26
# despues ya da cosas raras
"""
Created on Thu Sep  6 18:32:06 2012

@author: Calderon Apolinar Marco A
"""

from math import exp 
x=eval(raw_input("dame un valor para calcular la exponencial"))
y=exp(-x)
s=1
n=1
d=1.
i=1.
while i<100:
    n=n*x
    d=d*i
    s=s+(-1.)**i*(n/d)
    i=i+1
r=((abs(y-s))/y)*100
print "el valor calculado es %f " %s
print "el valor  exacto   es %f " %y
print "el error porc entre los valores es %f " %r