from euler import *
from scipy.integrate import ode
def f(t,y): return 1-t*y
r=ode(f)
r.set_initial_value(1.0,0)
t1=5.00
dt=0.01
tv=[]
yv=[]
while r.successful() and r.t < t1:
    tv.append(r.t)
    yv.append(float(r.y))
    r.integrate(r.t+dt)
t,y=euler(f,0,5,1,0.01)
print 'ti   yi(Aproximado) yi(Verdadero)  Error'
print'________________________________________'
i=0
for k in t:
    print '%3.2f   %9.5f   %9.5f   %9.5f' %(k,y[i],yv[i],abs(yv[i]-y[i]))
    i=i+1
