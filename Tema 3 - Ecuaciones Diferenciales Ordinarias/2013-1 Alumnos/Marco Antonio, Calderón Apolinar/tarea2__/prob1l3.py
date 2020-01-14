# problema 1, lista 3, diferenciales
"""
@author: Calderon Apolinar Marco A.
"""

n=3
x=[2.36,2.37,2.38,2.39]
f=[0.85866,0.86289,0.86710,0.87129]

def g(xa):
 yres=0
 for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i!=j:
            z=z*(xa-x[j])/(x[i]-x[j])
    yres=yres+z*f[i]
    
 return yres

r=eval(raw_input('dame un valor'))

h=0.1 
z=(-g(r+2*h)+4*g(r+h)-3*g(r))/(2*h)
w=(2*g(r)-5*g(r+h)+4*g(r+2*h)-g(r+3*h))/(h**2)
print 'la primera derivada en',r,'es:', z
print 'la segunda derivada en',r,'es:', w