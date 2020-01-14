import numpy as np
import matplotlib.pyplot as plt
g=9.8
m=1
k=np.arange(0.1,10.0,.1)
#RAMIREZ MORALES FRANCISCO JAVIER
km1=1/k

vt=(m*g)*km1
p=m*km1

plt.plot(vt,p,'bo')
plt.xlabel('velocidad terminal(m*g/k)')
plt.xlabel('m/k')
plt.title('velocidad terminal contra m/k')
plt.grid()
plt.show()

