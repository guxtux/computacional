from pylab import*
#RAMIREZ MORALES FRANCISCO JAVIER
# este codigo obtiene la serie de fibonacci con la siguiente formula
b=[]

 
m=3
while 3 <= m <50:
         b.insert(m,(1.0/sqrt(5.0))*((0.5*(1+sqrt(5.0)))**m)-((0.5*(1-sqrt(5.0)))**m))    
         m=m+1
         

print b

