import numpy as np
from math import pi
n=4
x=np.linspace(0,2*pi,5)
f=np.array([0.00000000e+00,1.00000000e+00,1.22464680e-16,-1.00000000e+00,-2.44929360e-16])
xa=eval(raw_input('Dame el valor de x:'))

yres=0

for i in range(0,n+1):
	z=1.0
	for j in range(0,n+1):
		if i!=j:
			z=z*(xa-x[j])/(x[i]-x[j])
	yres=yres+z*f[i]
print 'El polinomio evaluado en p(',xa,')=', yres