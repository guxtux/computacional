#este codigo sirve para evaluar exp(-x) en x=0.1
#el valor obtenido es tal que el error absoluto es menor que 10e-8
from pylab import *
#RAMIREZ MORALES FRANCISCO JAVIER
def factorial(n):
   
     f = 1
     while (n > 0):
        f = f * n
        n = n - 1
        
     return f

val1=0.904837418035959  # este es el valor exacto para x=.1 
x1=.1
exp1=0.0
for n in range(1,10000000):
    exp1=exp1+((-1)**n)*(x1**n)/factorial(n)
    if abs(val1-(exp1+1))/val1 < 1e-10:
        break

print ' exp(-x) en x=.1 es:' ,exp1 +1 # le sumo uno pues el factorial que defini no vale para n=0

    
    

     
