# -*- coding: cp1252 -*-
from scipy import*
from scipy. integrate import romberg

Teta0=array([15,30,45]) # valores en grados
Tr=Teta0*(2*pi/360)# valores en radianes

def  f1(x):return (1-((sin(Tr[0]/2))**2)*(sin(x))**2)**(-0.5)
def  f2(x):return (1-((sin(Tr[1]/2))**2)*(sin(x))**2)**(-0.5)
def  f3(x):return (1-((sin(Tr[2]/2))**2)*(sin(x))**2)**(-0.5)
R=[]

r1=romberg(f1,0,pi/2,show=False)
r2=romberg(f2,0,pi/2,show=False)
r3=romberg(f3,0,pi/2,show=False)
R.append(r1),R.append(r2),R.append(r3)
#comparando con el valor de oscilaciones pequeñas

H=pi/2
E=[]
E1=(abs(H-r1)/H)*100
E2=(abs(H-r2)/H)*100
E3=(abs(H-r3)/H)*100

E.append(E1),E.append(E2),E.append(E3)



print ' angulo en grados   h(angulo)    Error relativo       '
print '***********************************************'
for i in range(len(Tr)):
    print ' %4.2f  %9.9f %9.9f' %(Teta0[i],R[i],E[i])

