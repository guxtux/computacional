# problema 2, lista 3, segunda derivada
"""
@author: Calderon Apolinar Marco A
"""
n=3
x=[0.84,0.92,1.,1.08,1.16]
f=[0.431711,0.398519,0.367879,0.339596,0.312486]

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
def w(r,h):
  return (2*g(r)-5*g(r+h)+4*g(r+2*h)-g(r+3*h))/(h**2)
  
# extrapolacion de Richardson
z=w(r,0.92)
k=w(r,0.84)
der=(2**2*k-z)/(2**2-1)
print 'la segunda derivada en',r,'es:', der