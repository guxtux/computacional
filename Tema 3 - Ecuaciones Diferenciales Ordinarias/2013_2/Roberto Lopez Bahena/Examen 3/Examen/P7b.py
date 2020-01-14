from RK2SYSTEM import *
import matplotlib.pyplot as plt
def f(t,y,z): return -(2.0/50)*y
def g(t,y,z): return -(3.0/20)*z+(2.0/20)*y
t,y,z=RK2SYSTEM(f,g,0,60,10,0,0.025)
print 'La maxima concentracion es:',max(z),'onza/galon'
plt.plot(t,y)
plt.grid(True)
plt.show()
