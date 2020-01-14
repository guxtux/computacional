from Eulersystem import *
import matplotlib.pyplot as plt
def f(t,y,z): return z
def g(t,y,z): return -2.0*9.8*y
t,y,z=Eulersystem(f,g,0.0,10.0,1.002,0,0.001)
i=0
while y[i]!=max(y):
    i=i+1
tmax=t[i]
print 'El maximo de ya es:',max(y),'Lo alcanza en el tiempo:',tmax
i=0
while y[i]!=min(y):
    i=i+1
tmin=t[i]
print 'El minimo de ya es:',min(y),'Lo alcanza en el tiempo:',tmin
plt.plot(t,y)
plt.grid(True)
plt.show()
