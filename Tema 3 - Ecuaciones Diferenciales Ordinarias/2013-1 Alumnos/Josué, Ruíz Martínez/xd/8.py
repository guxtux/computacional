#Josue Ruiz Martinez
from math import*
import numpy as np
from numpy import*
import matplotlib.pyplot as plt
from scipy import*
from scipy.integrate import romberg
u=0.0
h=0.05
I=[]
I.append(0)
for i in range (20):
    u=u+h
    def f(x): return ((u**3)*((x**4)*exp(x)))/(exp(x)-1)
    r=romberg(f,0.,1./u,show = True)
    I.append(r)
w = linspace(0.0, 1.0, 19)
plt.plot(w, I)
plt.show()
