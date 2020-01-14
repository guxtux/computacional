from pylab import*
# encontramos el intervalo en el que hay un cambio de signo y por lo tanto una raiz
def f(x): return x-tan(x)
z=range(0,21,1)
for i in z:
   k=[] 
   k[i]=(z[i],z[i+1])
print k
a,b,dx=(0,20,0.01)

def buscaraiz(f,a,b,dx):

    
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2> 0.0 :
        if x1>= b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2
    

   

        
        

print ' el intervalo es:'
x1,x2= buscaraiz(f,a,b,dx)
print x1,x2

ec=raw_input('dame la funcion a evaluar')#pedimos la funcion a evaluar
errordeseado=input('da la tolerancia')#pedimos la tolerancia

def biseccion(x1,x2):
    return eval(ec)#eval evalua una cadena
#iniciamos un ciclo while
while True:
    xmed=(x1+x2)/2 #obtenemos el punto medio entre x1 y x2
    fxmed=f(xmed)# valor de la funcion en el punto medio
    if fxmed==0.0:# si fxmed es 0 entonces esta es la raiz
        break#por lo tanto salimos
    if (f(x1)*f(xmed))<0: #si este producto es negativo entonces la raiz esta entre x1 y xmed
        x1=x2 # actualizamos los valores de x1 y x2 para la siguiente iteracion
        x2=xmed
    else:# si el producto es positivo esta entre xmed y x2
        x1=xmed# actualizamos los valores
        x2=x2
    error=abs(x2-x1)# el error es el valor absoluto de la diferencia entre x2 y x1
    if error<errordeseado: # si el error es menor que la tolerancia
        break#salimos del while  e imprimimos el resultado
print ' el valor de la raiz es ', xmed


    # para x-tan(x)
 #(a,b)=(0,1) pasos de 0.01  
# el intervalo es:
#0.0, 0.01
# el valor de la raiz es  0.009921875

#(a,b)=(4,5) pasos de 0.01
#el intervalo es:
#4.49, 4.5
#el valor de la raiz es  4.495078125

#(a,b)=(7,8) pasos de 0.01
#el intervalo es:
#7.72, 7.73
# el valor de la raiz es  7.727578125
#(a,b)=(10,11) pasos de 0.1
#el intervalo es:
#10.9 10.91
# el valor de la raiz es  10.905078125

