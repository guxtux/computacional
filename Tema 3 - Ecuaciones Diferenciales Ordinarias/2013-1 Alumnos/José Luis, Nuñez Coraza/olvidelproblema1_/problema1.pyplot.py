import matplotlib as plt
from math import *
from numpy import as np

t=np.arange(0,2*pi,0.1)
a=328.33
b=20.33
r=1/sqrt((1/a)*math.sen(t)**2+(1/b)*math.cos(t)**2)    #f(x)=

plt.plot(t,r)
plt.show()