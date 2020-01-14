from RK4SYSTEM import *
import matplotlib.pyplot as plt
def f(t,y,z): return z
def g1(t,y,z): return 2.0*t-((0.4096)**2)*y-2*(0.4096)*(0.5)*z
def g2(t,y,z): return 2.0*(1-t)-((0.4096)**2)*y-2*(0.4096)*(0.5)*z
def g3(t,y,z): return -((0.4096)**2)*y-2*(0.4096)*(0.5)*z
t1,y1,z1=RK4SYSTEM(f,g1,0.0,1.0,0,0,0.01)
t2,y2,z2=RK4SYSTEM(f,g2,1.001,2.0,0,0,0.01)
t3,y3,z3=RK4SYSTEM(f,g3,2.001,10.0,0,0,0.01)
t=t1+t2+t3
y=y1+y2+y3
plt.plot(t,y)
plt.grid(True)
plt.show()
