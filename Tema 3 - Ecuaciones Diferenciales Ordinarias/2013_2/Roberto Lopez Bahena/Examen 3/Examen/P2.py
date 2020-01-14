from euler import *
import math
import matplotlib.pyplot as plt
def f(t,y): return (-3*((0.02)**2)*math.sqrt(2*9.8*y))/(((0.25*y)**2)+((0.02)**2)+(0.25*y)*(0.02)+(2*(0.25*y)+(0.02)*(0.25)))
t,y=euler(f,0,24.65,0.5,0.001)
i=0
while y[i] > 0.001:
    i=i+1
print 'El tiempo que se tarda en vaciar es:',t[i]
plt.plot(t,y)
plt.grid(True)
plt.show()
    
                                         
