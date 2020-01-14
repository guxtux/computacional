# sucesion de fibonacci 1,1,2,3,4,5,8 a partir de una recurrencia lineal
#RAMIREZ MORALES FRANCISCO JAVIER
l1=1#primer elmento de la sucesion
l2=2#segundo elemento de la sucesion
a=range(2,50)
a.insert(0,1)
a.insert(1,1)

for i in range(2,50):
    
    a[i]=a[i-1]+a[i-2]
    
    print a[i]
