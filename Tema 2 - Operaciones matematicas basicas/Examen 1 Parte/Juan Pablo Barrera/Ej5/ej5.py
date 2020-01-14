from nevilleinter import *

#Calcula la densidad del aire a 10.5 km de altura
#Se utiliza el metodo de neville porque es el metodo mas eficiente para calcular un punto. El de newton calcula todo el polinomio de
#interpolacion y el de neville lo va aproximando tomando solamente los datos que necesita.
import matplotlib.pyplot as plt

h=[0, 1.525, 3.050, 4.575, 6.10, 7.625, 9.150]
ro=[1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]

plt.plot(h,ro)
plt.hold(True)

ro0=neville(h,ro,10.5)
print("La densidad del aire a 10.5km de altura es %3.5f"%ro0)

plt.plot(10.5,ro0,"s")
plt.grid()
plt.show()
