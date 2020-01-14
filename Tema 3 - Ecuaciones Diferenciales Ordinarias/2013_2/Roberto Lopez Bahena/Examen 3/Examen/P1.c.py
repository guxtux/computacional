from euler import *
import math
def f(t,y):return (t**2)-y
def fv(t): return (t**2)-2*t+2+(-1.5)*math.exp(-t)
t,y=euler(f,0,5,0.5,0.01)
i=0
print 'ti   yi(Aproximado) yi(Verdadero)  Error'
print'________________________________________'
for k in t:
    print '%3.2f   %9.5f   %9.5f   %9.5f' %(k,y[i],fv(k),abs(fv(k)-y[i]))
    i=i+1
