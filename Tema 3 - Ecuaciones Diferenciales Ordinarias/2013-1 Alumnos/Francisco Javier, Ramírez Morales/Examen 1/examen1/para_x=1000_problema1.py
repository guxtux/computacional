#este codigo sirve para evaluar exp(-x) en x=1000
#el valor obtenido es tal que el error absoluto es menor que 10e-8
from pylab import *
#RAMIREZ MORALES FRANCISCO JAVIER
def factorial(n):
   
     f = 1
     while (n > 0):
        f = f * n
        n = n - 1
        
     return f
val5=5.0759588975e-435   #para x=1000

x5=1000.0
exp5=0.0
for n in range(1,10):
    exp5=exp5+((-1)**n)*(x5**n)/factorial(n)
    if abs(val5-(exp5+1))/val5 < 1e-10:
        break

print ' exp(-x) en x=1000 es:' ,exp5 +1 # le sumo uno pues el factorial que defini no vale para n=0
# para este valor vemos que los resultados se alejan mucho del valor exacto
# el valor exacto es del orden del epsilon absoluto y por lo tanto se interpreta como 0
#por lo que no podemos comparar el error
