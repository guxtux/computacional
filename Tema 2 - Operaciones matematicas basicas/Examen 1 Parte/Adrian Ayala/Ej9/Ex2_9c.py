# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 01:22:35 2013

@author: acesimbrote
"""
from numpy import *
from funciones import *

def secante(a, b, m, tole, f ):
		c = eval(f.replace("x","a"))
		d = eval(f.replace("x", "b"))
		er = tole + 1
		i = 0
		x2 = 0
		while c != 0 and er > tole and i < m and d - c != 0:
			x2 = b - (d*(b-a)) / (d-c)
			y2 = eval(f.replace("x","x2"))        
			er = abs(x2 - b)
			i = i + 1
			a = b
			c = d
			b = x2
			d = y2
		if c == 0:
				print str(a) + " es raiz"
		else:
				if er < tole:
						print str(a), " es raiz con un error: ", er
                                  
				else:
						if d - c == 0:
								print "Division por cero"
						else:
								print "No se encontro la raiz"


print 'De la función f(x)=x + 1/((x+3)*x' 
secante(-3.5,3,1000,0.001,'x + 1/((x+3)*x)')
#secante(0.3,0.4,1000,0.001,'log(x)-0.2*x**2 +1')
#secante(-3.5,3,1000,0.001,'0.1*x**3-5*x**2-x+4+exp(-x)')

