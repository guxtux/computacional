#este codigo sirve para evaluar exp(-x) en x=100
#el valor obtenido es tal que el error absoluto es menor que 10e-8
from pylab import *
#RAMIREZ MORALES FRANCISCO JAVIER
def factorial(n):
   
     f = 1
     while (n > 0):
        f = f * n
        n = n - 1
        
     return f
val4=3.72007597602e-44 #para x=100
x4=10.0
exp4=0.0
for n in range(1,100):
    exp4=exp4+((-1)**n)*(x4**n)/factorial(n)
    if abs(val4-(exp4+1))/val4 < 1e-10:
        break

print ' exp(-x) en x=100 es:' ,exp4 +1 # le sumo uno pues el factorial que defini no vale para n=0
# para este valor vemos que los resultados se alejan mucho del valor exacto
#el resultado que obtenemos en x=100 es: 4.53999294341e-05
