# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:38:46 2012

@author: pako
"""
import math
print("Este programa calcula la velocidad de un oscilador amortiguado a un tiempo t")
V=eval(raw_input("Máximo de la oscilación en m/s: "))
a=eval(raw_input("Factor de amortiguamiento en Hz: "))
w=eval(raw_input("Velocidad angular de oscilación en rad/s: "))
t=eval(raw_input("Tiempo al que se desea conocer la posición en segundos: "))
e=math.exp(-a*t)
c=math.cos(w*t)
v=V*e*c
print "La velocidad del oscilador en t =",t,"s es:",v,"m/s"