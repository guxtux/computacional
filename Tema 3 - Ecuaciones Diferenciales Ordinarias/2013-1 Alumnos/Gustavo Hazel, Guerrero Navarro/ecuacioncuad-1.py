# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/est5/.spyder2/.temp.py
"""
a=eval(raw_input('de el valor del coeficiente de x²:'))
b=eval(raw_input('de el valor del coeficiente de x:'))
c=eval(raw_input('de el valor del coeficiente constante:'))

discr=b**2 - 4*a*c
if discr>0:
  if a>0:
     x1=(-b + (b**2 -4*a*c)**0.5)/(2*a)
     x2=(-b - (b**2 -4*a*c)**0.5)/(2*a)
     print 'las soluciones a la ecuación cuadrática son','x1=', x1, 'x2=', x2
  elif a==0:
     x11=(-2.*c)/(b+(b**2. - 4.*a*c)**0.5)
     x22=(-2.*c)/(b-(b**2. - 4.*a*c)**0.5) 
     print 'las soluciones a la ecuación cuadrática son','x1=', x11, 'x2=', x22
  else:
     print 'no se me ocurre' 
     
else:
   print 'las soluciones son complejas'    

x1=(-b + (b**2 -4*a*c)**0.5)/(2*a)
x2=(-b - (b**2 -4*a*c)**0.5)/(2*a)
x11=(-2.*c)/(b+(b**2. - 4.*a*c)**0.5)
x22=(-2.*c)/(b-(b**2. - 4.*a*c)**0.5)    

e1=(abs((x1-x11)/x1))*100  
e2=(abs((x2-x22)/x2))*100

print 'los errores relativos son:', e1 ,'y', e2 
 