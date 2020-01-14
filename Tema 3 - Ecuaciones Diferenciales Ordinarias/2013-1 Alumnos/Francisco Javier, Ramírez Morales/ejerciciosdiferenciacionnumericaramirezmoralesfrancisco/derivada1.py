from pylab import*

# queremos la derivada en x=2.36
x=np.array([2.36,2.37,2.38,2.39],float)# datos que tenemos
f=np.array([0.85866,0.86289,0.86710,0.87129],float)#valor de la funcion en estos datos
h=eval(raw_input('dame el valor del incremento'))
xs=eval(raw_input('dame el valor donde se evalua la derivada'))



# por el metodo de diferencias finitas tenemos lo siguiente para valores hacia adelante
dfx= (-f[2]+4*f[1]-3*f[0])/(2*h)
d2fx=(2*f[0]-5*f[1]+4*f[2]-f[3])/(h*h)
print ' la  primer derivada en el punto elegido es: ',dfx
print ' la segunda derivada en el punto elegido es',d2fx
