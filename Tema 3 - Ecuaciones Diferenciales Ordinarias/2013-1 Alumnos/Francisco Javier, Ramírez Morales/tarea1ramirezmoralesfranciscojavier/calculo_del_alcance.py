from pylab import *
A=0.93#m^2
ro=1.2#kg/m3
Vi=67#m/s
c=1
g=9.81#m/s^2
m=250#Kg
k=c*A*ro/2*m
t0=linspace(0,pi/2)

v0x=Vi*sin(t0)
v0y=Vi*sin(t0)
a=[]
#(g/k + v0y[1])*(x/v0x[1])+(g/k*k)*log(1-(x*k/v0x[1]))

print v0x[1]
print v0y[1]
ec=raw_input('De la funcion a resolver: ') 
#Pedimos los extremos
#input produce un número
#el float se asegura de conseguir un numero de punto flotante
#aunque se proporcione un entero
x1=float(input('de el extremo inferior del intervalo aproximado: '))
x2=float(input('de el extremo superior del intervalo aproximado: '))
errordeseado=input('De el error deseado: ')#Establecemos el error deseado
 
#Definimos una funcion f con un argumento x
#eval es un enunciado que produce código python a partir de una cadena
#entonces return eval(ec) devuelve el resultado de evaluar el string
#se proporcionó "ec"
def f(x):
    return eval(ec)
#Iniciamos un ciclo while
 
while True:
    xmed=(x1+x2)/2#calculamos el punto medio entre x1 y x2
    fxmed=f(xmed)#y en xmed
    if fxmed==0.0:#si fxmed es 0 pues es porque esta es la raiz
        break#salimos del while
 
    if (f(x1)*f(xmed))<0:#si es negativo entonces la raiz esta entre x1 y xmed
        x1=x1#actualizamos los valores
        x2=xmed
    else:#si es positivo, entonces esta entre xmed y x2
        x1=xmed#actualizamos los valores
        x2=x2
    error=abs(x2-x1)#el error es la diferencia entre x2 y x1 (valor absoluto)
    if error<errordeseado:#si el error es menor que el deseado,
        break#salimos del while
a.append(xmed) 
#imprimimos el resultado
print 'La raíz es',a

