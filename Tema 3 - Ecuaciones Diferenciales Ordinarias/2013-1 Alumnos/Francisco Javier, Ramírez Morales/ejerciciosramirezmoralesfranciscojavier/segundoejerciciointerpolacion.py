from pylab import*
n=4
x=linspace(0,2*pi,5)
f=sin(x)
yres=0
xa=eval(raw_input('dame el valor de x'))
#vamos a dividir al intervalo en incrementos de pi/4 para obtener la interpolacion de cada uno de esos puntos
for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i != j:
            z=z*(xa-x[j])/(x[i]-x[j])
    yres=yres+z*f[i]

print ' el polinomio evaluado en P(',xa,')=', yres

plot(x,f,'bo')
plot([0.78539816,1.570796,2.356194,3.141592,3.9269908,4.7123889,5.49778714],[0.874999998017,1.00000006935, 0.625000338072,5.54784247072e-07,-0.624999988284, -0.999999982942,-0.875000002207],'r*')
title('interpolacion lagrange')
xlabel('x') 
ylabel('sin(x)')
grid()
show()
#los puntos que dividen al intervalo [0,2*pi] en distancias de pi/4 son:
#array([0,0.78539816,1.570796,2.356194,3.141592,3.9269908,4.7123889,5.49778714,6.2831853])

#el polinomio evaluado en P( 0.78539816 )= 0.874999998017
#el polinomio evaluado en P(1.570796 )= 1.00000006935
#el polinomio evaluado en P( 2.356194 )= 0.625000338072
#el polinomio evaluado en P(3.141592  )= 5.54784247072e-07
#el polinomio evaluado en P(3.9269908)=  -0.624999988284
#el polinomio evaluado en P(4.7123889  )= -0.999999982942
#el polinomio evaluado en P(5.49778714 )=-0.875000002207


#LOS VALORES EXACTOS QUE PROPORCIONA EL MODULO MATH SON

#el polinomio evaluado en f(  0.78539816 )= .707106
#el polinomio evaluado en f( 1.570796 )=1 
#el polinomio evaluado en f(2.356194)=.707106
#el polinomio evaluado en f( 3.141592)=1.224646e-16
#el polinomio evaluado en f(3.9269908 )=-.707106 
#el polinomio evaluado en f( 4.7123889 )= -1
#el polinomio evaluado en f(5.49778714)= -.707106


#CON ESTO EL ERROR PARA CADA DATO ES:

#PARA X= 0.78539816 Er=.707106-0.874999998017=-0.167893998017
#PARA X=1.570796  Er=1-1.00000006935=-0.00000006935
#PARA X=2.356194  Er=.707106-0.625000338072=0.082105661928
#PARA X=3.141592  Er=1.224646e-5.54784247072e-07=0.000011691675752928
#PARA X=3.9269908   Er=.707106- (-0.624999988284)=
#PARA X= 4.7123889 Er=-1-(-0.999999982942) =
#PARA X=5.49778714  Er=-.707106-(-0.875000002207) =




