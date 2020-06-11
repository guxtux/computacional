# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:31:11 2017

@author: Master Chief
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import time


def MCint_area(f, a, b, n, m):
    porDebajo = 0 # counter for no of points below the curve
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            porDebajo += 1
    area = porDebajo/float(n)*m*(b-a)
    
    return area

def MCint3_area(f, a, b, n, m, N=1000):
    # Store every N intermediate integral approximations in an
    # array I and record the corresponding k value.
    I_values = []
    k_values = []
    below = 0  # counter for no of points below the curve
    for k in range(1, n+1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            below += 1
        area = below/float(k)*m*(b-a)
        if k % N == 0:
            I = area
            I_values.append(I)
            k_values.append(2*k)
    return k_values, I_values

def f1(x):
    return 2 + 3*x

a = 1; b = 2; n = 1000000; N = 10000; fmax = f1(b)

t0 = time.clock()
print (MCint_area(f1, a, b, n, fmax))
t1 = time.clock()
print (MCint_area_vec(f1, a, b, n, fmax))
t2 = time.clock()
print ('loop/vectorized fraction:', (t1-t0)/(t2-t1))

k, I = MCint3_area(f1, a, b, n, fmax, N)
print (I[-1])

error = 6.5 - np.array(I)

plt.plot(k, error, label='Monte Carlo integration')
plt.xlabel('number of samples')
plt.ylabel('error')
plt.savefig('tmp.pdf')
plt.show()