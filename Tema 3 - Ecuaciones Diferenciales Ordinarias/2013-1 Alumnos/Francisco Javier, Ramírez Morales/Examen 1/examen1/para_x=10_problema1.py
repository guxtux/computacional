#este codigo sirve para evaluar exp(-x) en x=10
#el valor obtenido es tal que el error absoluto es menor que 10e-8
from pylab import *
#RAMIREZ MORALES FRANCISCO JAVIER
def factorial(n):
   
     f = 1
     while (n > 0):
        f = f * n
        n = n - 1
        
     return f
val3=4.539992976248e-5#para x=10
x3=10.0
exp3=0.0
for n in range(1,100):
    exp3=exp3+((-1)**n)*(x3**n)/factorial(n)
    if abs(val3-(exp3+1))/val3 < 1e-10:
        break

print ' exp(-x) en x=10 es:' ,exp3 +1 # le sumo uno pues el factorial que defini no vale para n=0
# podemos notar que para este valor  x=10  el resultado es: 4.53999294341e-05
# tenemos una buena aproximacion
