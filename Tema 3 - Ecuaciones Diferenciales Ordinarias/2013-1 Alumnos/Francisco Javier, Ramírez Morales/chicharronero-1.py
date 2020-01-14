# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 10:50:29 2012

@author: vaio
"""
miarchivo = open('chicharronero_z2.dat','w')
from math import sqrt

a=eval(raw_input('dame a'))
if a==0: 
    print ' imposible partir por cero vuelve a correr el programa'
if a!=0:
    

    b=eval(raw_input('dame b'))
    c=eval(raw_input('dame c'))
    
    
if ((b**2)-4*a*c)>=0:


    
    g= sqrt((b**2)-4*a*c)
    x1 = (-b + g )/(2*a)
    x2 = (-b - g )/(2*a)
    x3 = (-2*c)/(b+ g)
    x4 = (-2*c)/(b- g)
    Er1=(abs((x1-x3)/x1))*100
    Er2=(abs((x2-x4)/x2))*100
    
    print ' el valor de x1 es x1= %9.9f' %x1 
    print ' el valor de x2 es x2= %9.9f' %x2
    print ' el valor de x3 es x3= %9.9f' %x3
    print ' el valor de x4 es x4= %9.9f' %x4
    print ' el valor del error para la primer raiz es : Er1= %9.9f'%Er1
    print ' el valor del error para la segunda raiz es: Er2=%9.9f'%Er2
    miarchivo.write(' x1 %9.9d x2 %9.9d x3 %9.9d  x4%9.9d Er1%9.9d Er2%9.9d ' %(x1,x2,x3,x4,Er1,Er2))
    miarchivo.close()
    
elif ((b**2)-4*a*c)<0:
     import cmath
     
     
     g=cmath.sqrt((b**2)-4*a*c)
     x1 = (-b + g )/(2*a)
     x2 = (-b - g )/(2*a)
     x3 = (-2*c)/(b+ g)
     x4 = (-2*c)/(b- g)
        
     print 'las soluciones son complejas y son'
     print' x1= ' ,x1
     print' x2= ' ,x2
     print' x3= ' ,x3
     print' x4= ' ,x4
     

    
       
    