#motocicleta

from math import sin, cos

A=0.93
m=250
rho=1.2
c=1
v=67
g=9.81
xmax=[]
 
k=(c*A*rho)/(2*m)
theta=arange(0.0,  3.141592/2, 0.1)
n=len(theta)
k=n
while n>0:
      n=n-1
      xmax=a.append(  (v**2)*sin(2*theta)/g - (4/3)*(v**3)*(sin(2*theta))*sin(theta)*k/(g**2)   )
      theta2=a.append(k-n)             #una lista que enumera el angulo correspondiente en theta para cada xmax

print 'el valor máximo de alcance es' max{xmax}
print 'y el ángulo correspondiente es'
