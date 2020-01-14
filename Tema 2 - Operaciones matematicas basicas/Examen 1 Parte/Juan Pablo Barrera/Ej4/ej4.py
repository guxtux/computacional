from newtonpoli import *
#se usa el metodo de newton porque se tienen que calcular diferentes temperaturas. Con el método de Neville se usa todo el algoritmo
#cada vez que se quiere calcular un punto. En cambio con el metodo de newton se calculan los coeficientes del polinomio de
#interpolacion y se evaluan los puntos en el polinomio, lo que implica que se hacen menos calculos.

import matplotlib.pyplot as plt
#la viscosidad del agua varia de la siguiente forma

T=[0, 21.1, 37.8, 54.4, 71.1, 87.8, 100]
uk=[1.79, 1.13, 0.696, 0.519, 0.338, 0.321, 0.296]
puntos=[10,30,60,90]
plt.plot(T,uk)
plt.hold(True)
a=coefs(T,uk)
pto=[]
i=0
print("T(°C)     uk")
print("--------------")
for t in puntos:
    pto.append(evalpoli(a,T,t))
    print("%3.2f   %3.5f"%(t,pto[i]))
    i=i+1

   

plt.plot(puntos,pto,"s")
plt.grid()
plt.show()
