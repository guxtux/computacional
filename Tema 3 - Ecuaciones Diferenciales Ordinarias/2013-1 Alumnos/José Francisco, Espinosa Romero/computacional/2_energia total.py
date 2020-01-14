# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/pako/.spyder2/.temp.py
"""

print("Este programa calcula la energía total de un objeto en la superficie de la Tierra")
m=eval(raw_input("Masa del objeto en kg: "))
v=eval(raw_input("Velocidad del objeto en m/s: "))
h=eval(raw_input("Altura del objeto en metros: "))
EP=m*9.81*h
EK=.5*m*v**2
E=EP+EK
print("La energia potencial del objeto es: "),(EP),("Joules")
print("La energia cinética del objeto es: "),(EK),("Joules")
print("La energia total del objeto es: "),(E),("Joules")