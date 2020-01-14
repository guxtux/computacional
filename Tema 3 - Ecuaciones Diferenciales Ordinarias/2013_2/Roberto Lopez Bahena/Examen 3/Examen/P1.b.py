from euler import *
import math
def f(t,y):return math.exp(-t) - 3*y
def fv(t): return (1.0/2)*(math.exp(-t)+math.exp(-3*t))
t,y=euler(f,0,5,1,0.01)
i=0
print 'ti   yi(Aproximado) yi(Verdadero)  Error'
print'________________________________________'
for k in t:
    print '%3.2f   %9.5f   %9.5f   %9.5f'%(k,y[i],fv(k),abs(fv(k)-y[i]))
    i=i+1

