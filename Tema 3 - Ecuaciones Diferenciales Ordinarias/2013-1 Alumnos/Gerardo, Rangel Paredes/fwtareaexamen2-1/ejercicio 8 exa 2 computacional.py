from math import*
import numpy as np
from numpy import*
import matplotlib.pyplot as plt
from scipy import*
from scipy.integrate import romberg

u = 0.0
h = 0.05
In = []
In.append(0)

for i in range (20):
    u = u + h
    def f(x): return ((u**3)*((x**4)*exp(x)))/(exp(x) - 1)
    resultado = romberg (f, 0., 1./u, show = True)
    In.append(resultado)

w = linspace(0.0, 1.0, 19)
plt.plot(w, In)
plt.xlabel("el valor de u")
plt.ylabel("el valor de la integral en funcion de u")
plt.show()
