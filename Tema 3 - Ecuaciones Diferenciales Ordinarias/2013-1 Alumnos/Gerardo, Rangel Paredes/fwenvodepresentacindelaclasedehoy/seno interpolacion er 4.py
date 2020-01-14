from math import*
import numpy as np
from numpy import* 
n = 4
x = linspace(0, 2*pi, 5)                          
f = np.array([0, 1.0, 0.,-1.0, 0])
xa = linspace(0, 2*pi, 9)
yres = 0
z = sin(xa)
for i in range(0, n + 1):
    z = 1.0
    for j in range(0, n + 1):
        if i != j:
            z = z*(xa- x[j])/(x[i]-x[j])
    yres = yres + z*f[i]

print "El polinomio de oreden 4 evaluado en P(",xa,") = ", yres
er = yres - z
print "El error de la funcion en la interpolacion es: ", er
