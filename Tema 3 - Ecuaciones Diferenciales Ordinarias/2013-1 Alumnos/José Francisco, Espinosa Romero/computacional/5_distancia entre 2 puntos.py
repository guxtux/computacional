# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:59:59 2012

@author: pako
"""

print("Este programa calcula la distancia entre 2 puntos en el plano")
x1=eval(raw_input("Coordenada x del primer punto: "))
y1=eval(raw_input("Coordenada y del primer punto: "))
x2=eval(raw_input("Coordenada x del segundo punto: "))
y2=eval(raw_input("Coordenada y del segundo punto: "))
p1=(x1,y1)
p2=(x2,y2)
d=(((x1-x2)**2)+((y1-y2)**2))**0.5
print "Primer punto: ",(p1)
print "Segundo punto: ",(p2)
print "La distancia entre los 2 puntos es: ",d

