from RK2 import *
import math
import matplotlib.pyplot as plt
def f(t,y): return -(2.0/50)*y
t,y=RK2(f,0,60,10,1)
i=0
while y[i] > 1.01:
    i=i+1
print 'El tiempo que tarda para que sea 1/10 de su valor inicial es:',t[i],'hr'
plt.plot(t,y)
plt.grid(True)
plt.show()

