from pylab import *


N=[2,4,8,16,32,64,128] # estos son los valores de N  para el metodo del trapecio extendido.
a=0.0# valor del punto x0 del intervalo
b=2.0#valor del punto xN del intervalo


h=[]
for i in range(len(N)):# se obtienen los valores de h para cada valor de N
    hi=(b-a)/N[i]
    h.append(hi)# estos valores se guardan en una lista


#para N[0] # para  N=2
xi0=[]
x=0
while x<b: # se ontienen los correspondientes xi
    x=x+h[0]
    xi0.append(x)# estos se guardan en una lista


#para N[1] analogamente para N=4

xi1=[]
x=0
while x<b:
    x=x+h[1]
    xi1.append(x)


#para N[2] N=8

xi2=[]
x=0
while x<b:
    x=x+h[2]
    xi2.append(x)

#para N[3] N=16

xi3=[]
x=0
while x<b:
    x=x+h[3]
    xi3.append(x)


#para N[4] N=32

xi4=[]
x=0
while x<b:
    x=x+h[4]
    xi4.append(x)

#para N[5] N=64

xi5=[]
x=0
while x<b:
    x=x+h[5]
    xi5.append(x)


#para N[6]   N=128

xi6=[]
x=0
while x<b:
    x=x+h[6]
    xi6.append(x)

def f(x): return pi*((1+(x/2)**2)**2) # esta es la funcion que queremos integrar 

fi0=[]
for z in xi0: # obtenemos los valores de f(xi) para N=2
    c=f(z)                     
    fi0.append(c)
fi1=[]
for z in xi1: # obtenemos los valores de f(xi) para N=4
    c=f(z)                     
    fi1.append(c)
fi2=[]
for z in xi2: # obtenemos los valores de f(xi) para N=8
    c=f(z)                     
    fi2.append(c)
fi3=[]
for z in xi3: # obtenemos los valores de f(xi) para N=16
    c=f(z)                     
    fi3.append(c)
fi4=[]
for z in xi4: # obtenemos los valores de f(xi) para N=32
    c=f(z)                     
    fi4.append(c)
fi5=[]
for z in xi5: # obtenemos los valores de f(xi) para N=64
    c=f(z)                     
    fi5.append(c)

fi6=[]
for z in xi6: # obtenemos los valores de f(xi) para N=128
    c=f(z)                     
    fi6.append(c)



# AHORA USAMOS LA  REGLA DEL TRAPECIO EXTENDIDA  PARA ENCONTRAR  EL VOLUMEN DEL CUERPO DE REVOLUCION
# EL VALOR EXACTO DEL VOLUMEN ES I= 11.7286


#  LA REGLA ES Ii=[f(x(i))+f(x(i+1))]*h/2
# PARA N=2 usamos fi0 que es la lista que contiene los valores de f(xi) y el correspondiente valor de h
i0=[]
p0=len(fi0)-1
j=0
for i in range(p0):
     j=fi0[i]+fi0[i+1]
     i0.append(j)
w0=sum(i0) 


I0=w0*(h[0]/2.0) #El valor de la integral para N=2 es 8.7375545678

# PARA N=4 usamos fi1 que es la lista que contiene los valores de f(xi) y el correspondiente valor de h
i1=[]
p1=len(fi1)-1
j=0
for i in range(p1):
     j=fi1[i]+fi1[i+1]
     i1.append(j)
w1=sum(i1) 


I1=w1*(h[1]/2.0)#El valor de la integral para N=4 es  10.3175547793

# PARA N=8 usamos fi2 que es la lista que contiene los valores de f(xi) y el correspondiente valor de h
i2=[]
p2=len(fi2)-1
j=0
for i in range(p2):
     j=fi2[i]+fi2[i+1]
     i2.append(j)
w2=sum(i2) 


I2=w2*(h[2]/2.0)#El valor de la integral para N=8 es  10.9962454042


# PARA N=16 usamos fi3 que es la lista que contiene los valores de f(xi) y el correspondiente valor de h
i3=[]
p3=len(fi3)-1
j=0
for i in range(p3):
     j=fi3[i]+fi3[i+1]
     i3.append(j)
w3=sum(i3) 


I3=w3*(h[3]/2.0)#El valor de la integral para N=16 es  11.3507357808

# PARA N=32 usamos fi4 que es la lista que contiene los valores de f(xi) y el correspondiente valor de h
i4=[]
p4=len(fi4)-1
j=0
for i in range(p4):
     j=fi4[i]+fi4[i+1]
     i4.append(j)
w4=sum(i4) 


I4=w4*(h[4]/2.0)#El valor de la integral para N=32 es  11.536161607


# PARA N=64 usamos fi5 que es la lista que contiene los valores de f(xi) y el correspondiente valor de h
i5=[]
p5=len(fi5)-1
j=0
for i in range(p5):
     j=fi5[i]+fi5[i+1]
     i5.append(j)
w5=sum(i5) 


I5=w5*(h[5]/2.0)#El valor de la integral para N=64 es  11.631436473


# PARA N=128 usamos fi6 que es la lista que contiene los valores de f(xi) el correspondiente valor de h
i6=[]
p6=len(fi6)-1
j=0
for i in range(p6):
     j=fi6[i]+fi6[i+1]
     i6.append(j)
w6=sum(i6) 


I6=w6*(h[6]/2.0) #El valor de la integral para N=64 es  11.6797778547

# AHORA CALCULAMOS LOS ERRORES RELATIVOS PARA CADA N
I= 11.7286 # este es el valor exacto

E0=(abs(I-I0)/I)*100 #N=2
E1=(abs(I-I1)/I)*100 #N=4
E2=(abs(I-I2)/I)*100 #N=8
E3=(abs(I-I3)/I)*100 #N=16
E4=(abs(I-I4)/I)*100 #N=32
E5=(abs(I-I5)/I)*100 #N=64
E6=(abs(I-I6)/I)*100 #N=128

#AHORA IMPRIMIMOS LOS RESULTADOS

print 'N=2 el valor de la integral es I0= %f2.7   el  error es E0= %f2.7' %(I0,E0)
print 'N=4 el valor de la integral es I1= %f2.7  el  error es E1= %f2.7' %(I1,E1)
print 'N=8 el valor de la integral es I2= %f2.7  el  error es E2= %f2.7' %(I2,E2)
print 'N=16 el valor de la integral es I3= %f2.7  el  error es E3= %f2.7' %(I3,E3)
print 'N=32 el valor de la integral es I4= %f2.7  el  error es E4= %f2.7' %(I4,E4)
print 'N=64 el valor de la integral es I5= %f2.7  el  error es E5= %f2.7' %(I5,E5)
print 'N=128 el valor de la integral es I6= %f2.7  el  error es E6= %f2.7' %(I6,E6)


