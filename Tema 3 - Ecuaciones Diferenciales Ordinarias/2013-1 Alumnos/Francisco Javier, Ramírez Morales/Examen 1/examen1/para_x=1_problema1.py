#RAMIREZ MORALES FRANCISCO JAVIER
#este codigo sirve para evaluar exp(-x) en x=1
#el valor obtenido es tal que el error absoluto es menor que 10e-8
from pylab import *

def factorial(n):
   
     f = 1
     while (n > 0):
        f = f * n
        n = n - 1
        
     return f
val2=0.367879441171442# para x=1
x2=1.0
exp2=0.0
for n in range(1,100000):
    exp2=exp2+((-1)**n)*(x2**n)/factorial(n)
    if abs(val2-(exp2+1))/val2 < 1e-10:
        break

print ' exp(-x) en x=1 es:' ,exp2 +1 # le sumo uno pues el factorial que defini no vale para n=0
# el valor que obtenemos  en x=1 es: 0.367879441161 que es practicamente exacto




