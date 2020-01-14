import numpy as np
from math import pi
n=4
x=np.linspace(0,pi/2,5)
f=np.array([0.,0.15027943,0.55536037,1.08841993,1.57079633])
xa=eval(raw_input('Dame el valor de x:'))

yres=0

for i in range(0,n+1):
	z=1.0
	for j in range(0,n+1):
		if i!=j:
			z=z*(xa-x[j])/(x[i]-x[j])
	yres=yres+z*f[i]
print 'El polinomio evaluado en p(',xa,')=', yres