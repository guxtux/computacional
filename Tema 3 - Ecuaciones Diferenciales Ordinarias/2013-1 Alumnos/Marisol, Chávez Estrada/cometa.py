# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:06:35 2012

@author: marisolchavez
"""

# Este programa intenta modelar la trayectoria del cometa Halley, use el metodo de Runge Kutta

from numpy import*
from pylab import*

#-----------------------------------------------------------------------------------------------------------
#Estas son las ecuaciones de movimiento para el cometa halley en X 
#U1 y U2 so las funciones de posicion desconocidas

def faxial(tg,U1,dU1,U2,dU2): 
 

   j = dU1 

   return j



def gaxial(tg,U1,dU1,U2,dU2): 
   
   Pi = 3.14159

   q = (4*(Pi**2)*U1) / ((U1**2 + U2**2)**(3/2))
   
   return q



# Estas son las ecuaciones demovimiento para la componente Y

def f(tg,U1,dU1,U2,dU2):

 

   j = dU2 

   return j



def g(tg,U1,dU1,U2,dU2):


   Pi = 3.14159

   q = (4*(Pi**2)*U2) / ((U1**2 + U2**2)**(3/2))

   return q

#----------------------------------------------------------------------------------------------------------------
 




print "Da los datos que se te piden: intervalo de tiempo (a"
x1 = input()

print "intervalo de tiempo b)"
x2 = input()

print "El numero de pasos que quiere"
n = input()
 
h = (x2-x1)/n 

print "El valor de h (incremento para runge Kutta) es:", h 


#CONDICIONES INICIALES, tenemos posicion y velocidad para el afelio

#t[0] = 0.0
lt = [0.0]   #tiempo
#t = lt[0]

li = [0.0]   #y inicial
#i = li[0]
#ldi = [0.0]
ldi = [0.0] #velocidad en y 
#di = ldi[0]


lz = [34.76]  #posicion en x (afelio es la posicion inicial) 
                #5.20x10^12 m =34.76 UA
#z = lz[0]
ldz = [912] #velocidad en x (m/s)
#dz = ldz[0]


#Aqui cominza el metodo Runge Kutta a orden 4

for k in range(n):


   f1axial = faxial(lt[k],li[k],ldi[k],lz[k],ldz[k])
   g1axial = gaxial(lt[k],li[k],ldi[k],lz[k],ldz[k])

   f1 = f(lt[k],li[k],ldi[k],lz[k],ldz[k])
   g1 = g(lt[k],li[k],ldi[k],lz[k],ldz[k])



   taux1 = lt[k]


   zaux1 = lz[k]
   dzaux1 = ldz[k]

   iaux1 = li[k]
   diaux1 = ldi[k]



   taux2 = taux1+(h/2.0)

   zaux2 = zaux1+((h/2.0)*f1axial)
   dzaux2 = dzaux1+((h/2.0)*g1axial)

   iaux2 = iaux1+((h/2.0)*f1)
   diaux2 = diaux1+((h/2.0)*g1)




   f2axial = faxial(taux2,li[k],ldi[k],zaux2,dzaux2)
   g2axial = gaxial(taux2,li[k],ldi[k],zaux2,dzaux2)

   f2 = f(taux2,iaux2,diaux2,lz[k],ldz[k])
   g2 = g(taux2,iaux2,diaux2,lz[k],ldz[k])




   zaux2 = zaux1+((h/2.0)*f2axial)
   dzaux2 = dzaux1+((h/2.0)*g2axial)

   iaux2 = iaux1+((h/2.0)*f2)
   diaux2 = diaux1+((h/2.0)*g2)



   f3axial = faxial(taux2,li[k],ldi[k],zaux2,dzaux2)
   g3axial = gaxial(taux2,li[k],ldi[k],zaux2,dzaux2)

   f3 = f(taux2,iaux2,diaux2,lz[k],ldz[k])
   g3 = g(taux2,iaux2,diaux2,lz[k],ldz[k])



   taux2 = taux1+(h)

   zaux2 = zaux1+(h*f3axial)
   dzaux2 = dzaux1+(h*g3axial)

   iaux2 = iaux1+(h*f3)
   diaux2 = diaux1+(h*g3)



   f4axial = faxial(taux2,li[k],ldi[k],zaux2,dzaux2)
   g4axial = gaxial(taux2,li[k],ldi[k],zaux2,dzaux2)

   f4 = f(taux2,iaux2,diaux2,lz[k],ldz[k])
   g4 = g(taux2,iaux2,diaux2,lz[k],ldz[k])


   lt.append(lt[k] + h)

   lz.append(lz[k] + (h/6.0)*(f1axial + 2.0*f2axial + 2.0*f3axial + f4axial))
   

   ldz.append(ldz[k] + (h/6.0)*(g1axial + 2.0*g2axial + 2.0*g3axial + g4axial))

   li.append( li[k] + (h/6.0)*(f1 + 2.0*f2 + 2.0*f3 + f4) )

   ldi.append( ldi[k] + (h/6.0)*(g1 + 2.0*g2 + 2.0*g3 + g4) )

      
   
plot(li[:],lz[:],"o")  #Estamos graficando posiciones x y y
show()

#COMENTARIOS FINALES
    #Ademas de las posiciones calculamos las velocidades (en las listas ldz y ldi) 
    #No se obtiene la elipse esperada, posiblemente hya un error en mi metodo runge kutta