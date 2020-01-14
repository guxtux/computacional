import matplotlib.pyplot as plt
from euler import *
def f(t,y): return -0.1044*y
t,y=euler(f,0.0,40.0,1E5,0.05)
print 'La densidad numerica del yodo es:',y[-1],'en el tiempo:',t[-1]
plt.plot(t,y)
plt.grid(True)
plt.show()
