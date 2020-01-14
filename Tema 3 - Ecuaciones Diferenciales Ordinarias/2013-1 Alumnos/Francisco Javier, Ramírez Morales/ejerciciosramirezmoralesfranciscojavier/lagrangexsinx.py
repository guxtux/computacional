from pylab import *
n=4
x=linspace(0,pi/2,5)#tenemos 5 valores que son necesarios para que funcione el codigo para el grado 4
f=x*sin(x)
xa=eval(raw_input('dame el valor de x'))
#vamos a evaluar los puntos que dividen al intervalo [0,pi/2] en distancias de pi/16
yres=0
for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i != j:
            z=z*(xa-x[j])/(x[i]-x[j])
    yres=yres+z*f[i]

print ' el polinomio evaluado en P(',xa,')=', yres

plot(x,f,'bo')
plot([0.19634954,0.39269908,0.58904862,0.78539816,0.9817477,1.17809725,1.37444679],[0.0373880567038,0.150279431197,0.327681164071,0.555360362991,0.815844202702,1.08841993882,1.34913485137],'r*')
title('interpolacion lagrange')
xlabel('x') 
ylabel('x*sin(x)')
grid()
show()

# los valores  en distancias de  pi/16 en el intervalo [0,pi/2] son: linspace(0,pi/2,9)
# array([0,0.19634954,0.39269908,0.58904862,0.78539816,0.9817477,1.17809725,
#1.37444679,1.57079633])

#el polinomio evaluado en P( 0.19634954 )= 0.0373880567038
#el polinomio evaluado en P( 0.39269908 )= 0.150279431197
#el polinomio evaluado en P( 0.58904862 )= 0.327681164071
#el polinomio evaluado en P( 0.78539816 )= 0.555360362991
#el polinomio evaluado en P( 0.9817477 )=  0.815844202702
#el polinomio evaluado en P( 1.17809725 )= 1.08841993882
#el polinomio evaluado en P( 1.37444679 )= 1.34913485137


#LOS VALORES EXACTOS QUE PROPORCIONA EL MODULO MATH SON

#el polinomio evaluado en P( 0.19634954 )= 0.0383059
#el polinomio evaluado en P( 0.39269908 )= 0.15027943
#el polinomio evaluado en P( 0.58904862 )= 0.32725788
#el polinomio evaluado en P( 0.78539816 )= 0.55536037
#el polinomio evaluado en P( 0.9817477 )= 0.81629338
#el polinomio evaluado en P( 1.17809725 )= 1.08841993
#el polinomio evaluado en P( 1.37444679 )= 1.34803718


#CON ESTO EL ERROR PARA CADA DATO ES:

#PARA X=0.19634954  Er=0.0383059-0.0373880567038=0.0009178432962
#PARA X=0.39269908  Er=0.15027943-0.150279431197=-0.000000001197
#PARA X=0.58904862  Er=0.32725788-0.327681164071=-0.000423284071
#PARA X=0.78539816  Er=0.55536037-0.555360362991=0.000000007009
#PARA X=0.9817477   Er=0.81629338-0.815844202702=0.000449177298
#PARA X= 1.17809725 Er=1.08841993-1.08841993882 =-0.00000000882
#PARA X=1.37444679  Er=1.34803718-1.34913485137 =-0.00109767137







