# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:27:17 2013

@author: acesimbrote
"""

import math
import matplotlib.pyplot as plt
import numpy as np


a=[]
b=[]
g = 9.81
c = 1.0
A = 0.93
r = 1.2
m = 250.0
h = (c*A*r)/(2.0*m) #unidades [Kg^2 / m]
Te = eval(raw_input('Ángulo: '))
t = eval(raw_input('t = '))


#Al = 
Vo = 67 
Vox = Vo * math.cos(Te)  
Voy = Vo * math.sin(Te)  
#t = - (1/h) math.log((1-Al))

i=0

while i<t:
    
    x = Vox * (1 - math.exp(-h*i))
  #  d = (1/h)
 #   e = (Voy*h)+g
#    f = (1- (math.exp(-h*i)))
#    y = d * ( (e * f)  - (g*i))
    y = ( (Voy/h +(g/h**2.0)) * (1-(math.exp(-(h*i)))) ) - ((g*i)/h)
#    vel = ( (g * x) * (1 - math.exp(j))
    z = ((g*x) * (1 + j - math.exp(j))) + yo
    i= i + 0.5
    a.append(x)
    b.append(y)


plt.plot(x,y)
plt.show()    
#print 'x = ',x , 'y = ', y


    

