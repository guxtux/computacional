from RK2SYST3 import *
import matplotlib.pyplot as plt
import math
def f(t,u,v,x): return -0.005*math.sqrt((u**2)+(v**2))*u
def g(t,u,v,x): return -9.9-0.005*math.sqrt((u**2)+(v**2))*v
def h(t,u,v,x): return u
def h1(t,u,v,x): return v
t,u,v,x=RK2SYST3(f,g,h,0.0,12.2,150,150,0,0.01)
t,u,v,y=RK2SYST3(f,g,h1,0.0,12.2,150,150,0,0.01)
plt.plot(x,y)
plt.grid(True)
plt.show()
