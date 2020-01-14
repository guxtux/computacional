from RK4SYSTEM import *
import matplotlib.pyplot as plt
def f(t,y,z): return z
def g(t,y,z): return (1.0/5)-((0.4096)**2)*y-2*(0.4096)*(0.5)*z
t,y,z=RK4SYSTEM(f,g,0.0,10.0,0,0,0.01)
plt.plot(t,y)
plt.grid(True)
plt.show()
