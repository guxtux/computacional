#Josué Ruíz Martínez
#Problema 3
import numpy as np
import matplotlib.pyplot as plt
mus=open("caida.dat","w")
k=1
m=1
g=9.8
t=np.arange(0,10)
p=[]
q=[]
for i in reversed(t) :
	a=m*g*i/k
	b=m/k	
	c=m*-g/k
	d=i*-b/m
	e=m*g/k
	z=a+(b*c)*(1-np.exp(d))
	q.append(z)
	v=e+(c)*np.exp(d)
	p.append(v)	
	mus.write("%f %f\n" %(i,z))
	print z	, v
mus.close()
plt.figure('Caida libre: ')
plt.subplot(211)
plt.plot(t,Z,'g-')
plt.subplot(212)
plt.plot(t,V,'ro')
plt.show()    




