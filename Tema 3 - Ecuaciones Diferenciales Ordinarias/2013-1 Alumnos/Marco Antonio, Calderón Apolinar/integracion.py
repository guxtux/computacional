# integracion
"""
@author: Calderon Apolinar Marco A
"""
p=[2,4,8,16,32,64,128]
for N in p:
     from math import pi
     # valor de h
     b=2.0
     a=0.0
     h=(b-a)/N
    
     # particionamos el intervalo
     x=0
     particion=[]
     while x<=2:
      particion.append(x)
      x+=h
    
     # definimos la funcion
     v=[]
     def f(x): return pi*((1+(x/2.)**2)**2)
     for c in particion:
      y=f(c)
      v.append(y)
    
     # hacemos la suma
     def I(i):
      i=len(particion)-1
      y=(v[i]+v[i-1])*(h/2.0)
      while i>=1:
       i=i-1
       y=y+(v[i]+v[i-1])*(h/2.0)
      return y
     print y
    
