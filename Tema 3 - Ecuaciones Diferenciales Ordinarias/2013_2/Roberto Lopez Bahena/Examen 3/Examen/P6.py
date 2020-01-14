from Eulermodsyst import *
import matplotlib.pyplot as plt
def f(t,y,z): return -0.1044*y
def g(t,y,z): return -(0.0753*z)+(0.1044*y)
t,y,z=Eulermodsyst(f,g,0.0,50.0,1E5,0,0.1)
i=0
print 'ti   Densidad del Yodo-135    Densidad del Xenon-135'
print'_____________________________________________________'
for k in t:
    print '%3.1f      %9.5f         %9.5f' %(k,y[i],z[i])
    i=i+1
plt.plot(t,y)
plt.grid(True)
plt.show()
