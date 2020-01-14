#circulo

import numpy as num
import matplotlib.pyplot as plt


n=3
p=[]
steta=[]
steta.append(1)
p.append(4)
i=1
errabs=[]
p2=4.*num.arctan(1.)
while n<21:


    steta.append(steta[i-1]/((2*(1+(1-(steta[i-1]**2))**.5))**.5))
    p.append((2**(n-1))*steta[i])

    n=n+1
    i=i+1

    errabs.append(abs(p[i-1]-p2))
print("los valores de sin son:",steta)
print("los valores de p son:",p)
print("el error absoluto en cada iteracion:",errabs)

plt.plot(errabs)
plt.ylabel("error absoluto")
plt.xlabel("iteraciones")
plt.show()
#el error va disminuyendo con cada iteracion. El valor de pi se va acercando al caluculado con la tangente.
