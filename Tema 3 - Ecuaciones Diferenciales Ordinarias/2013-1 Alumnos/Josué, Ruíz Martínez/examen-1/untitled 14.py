#Josué Ruíz Martínez
#Problema 1
import numpy as np
import matplotlib.pyplot as plt
h=[48,100,70,-20,2]
z=np.arange(-4,-.5,.5)
b=[]
c=[]
for n in z:
	a=0
	for i in reversed(h):
		a=i+n*a
#Como ya lo habiamos hecho anteriormente utilizamos el metodo de Horner.
        print a
	b.append(a)
        c.append(n)
#Aqui guardamos los datos para poder graficarlos.
np.savetxt('test.out', (c,b),delimiter=',')
plt.figure('P= ')
plt.plot(c,b,'b-')
plt.show()

