from pylab import*
# encontramos el intervalo en el que hay un cambio de signo y por lo tanto una raiz
def f(x): return  1e5-8.311441*log((x/4.44418)**(5/2))*x


a,b,dx=(1,9000,0.01)# el valor de a es 1 pues no nos interesan temperaturas negativas

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
errordeseado=input('da la tolerancia')#pedimos la tolerancia en este caso 0.01

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

