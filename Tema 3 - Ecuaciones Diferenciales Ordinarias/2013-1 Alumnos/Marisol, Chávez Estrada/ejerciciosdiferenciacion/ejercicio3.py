# -*- coding: utf-8 -*-

"""
EJERCICIO 3

LA PALANCA AB DE RADIO R GIRA CON VELOCIDAD ANGULAR CONSTANTE
CALCULA LA ACELERACION ANGULAR DEL PISTON

@author: marisolchavez
"""


from math import *
from numpy import *
import numpy as np

#theta que es el angulo entre la barra AB y la horizontal
theta=0.0
fi = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
dphi = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
ddphi = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])


#las funciones que dependeran de theta, las separe en numerador y denminador

#el numerador indica la dependencia angular
def num(theta): 								 
	return np.cos(theta)+np.sqrt(2.5**2-np.sin(theta)*np.sin(theta))-5.25 

#el denominador se obtiene aplican la ley de cosenos
def den(theta): 
	return np.cos(theta)+np.sqrt(2.5**2-np.sin(theta)*np.sin(theta))

#phi= angulo entre el piston y la horizontal
def phi(teta):						 
	return np.arccos((num(theta))/(5.0*den(theta)))
fi[0]=phi(0)
print "phi=", phi(0),0					 
for n in range(0,36):    		#para cada theta
	theta= (5+5*n)*pi/180.0		#expresamos a theta en radianes
	fi[n+1]=phi(theta)			
	print "phi=", fi[n+1], "Theta(en radianes)=", theta		
	
#la derivada hacia adelante para el valor theta=0 y es llamado dphia
dphia=66.666667*((-3.0*fi[0]+4.0*fi[1]-fi[2])/(2*(5.0*pi/180))) 

#y se asocia el valor de la variable calculada llamada dphia con el elemento 0
# del arreglo dphi

dphi[0]=dphia							
print "Vel angular:", dphi[0]


#se inicia un ciclo for en el rango de valores 0 a 37
#Calcuamos las diferencias centrales para obtener la derivada en los puntos 
#centrales y se asocia con cada elemento del arreglo dphi

for i in range(0,36):						
	dphi[i+1]=66.666667*((fi[i+1]-fi[i])/(5.0*pi/180))	
	print "Vel angular:" ,dphi[i+1]	

#se calcula el ultimo valor mediante las diferencias hacia atras 
#para obtener la derivada en theta=180 grados:
    
dphib=66.6667*((-4.0*phi(175.0*pi/180.0)+phi(170.0*pi/180.0)+3.0*phi(180.0*pi/180.0))/(2.0*5.0*pi/180.0)) 														
dphi[36]=dphib			#se asocia dphib con el elemento 37 del arreglo
print "Vel angular", dphi[36]	

#Ahora calculamos la aceleracion:
    
print "La aceleracion angular es"

#por diferencias hacia adelante se calcula el primer elemento del arreglo ddphi 
#que corresponde a la segunda derivada  				
ddphia=(-3.0*dphi[0]+4.0*dphi[1]-dphi[2])/radians(5.0)			
ddphi[0]=ddphia						
print "Acel angular:", ddphi[0]

#se realiza el calculo de la aceleracion angular por medio de diferencias centrales
for i in range(0,36):
	ddphi[i+1]=(dphi[i+1]-dphi[i])/radians(5.0)			
	print "Acel angular", ddphi[i]						
 
#se calcula el valor de las diferencias hacia atras para el ultimo elemento 
ddphib=((-4.0*dphi[35]+dphi[34]+3.0*dphi[36])/(2.0*5.0*pi/180.0))		
ddphi[36]=ddphib
print "Acel angular", ddphi[36]
