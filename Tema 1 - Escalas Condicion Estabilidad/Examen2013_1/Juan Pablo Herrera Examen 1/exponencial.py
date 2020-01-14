#exponencial
import numpy as num

x=.1


valor=[]
err=[]
exp=[]
while x<10001:
    e=1.
    i=1
    fact=1
    pot=1.
    error=10
    while error>.00000008:
        fact=fact*i #termino del factorial
        pot=pot*x #termino de la potencia
        if i%2==0:
            e=e+pot/fact
        else:   
            e=e-pot/fact
        i=i+1
        error=abs(e-num.exp(-x))
    print("exp con la serie=",e)
    print("exp con la funcion",num.exp(-x))
    print("error absoluto=",error)
    exp.append(e)
    err.append(error)
    valor.append(x)
    x=x*10

print(exp)
#el valor de la funcion e^-x a partir del valor de cien es demasiado pequeño para ser calculado con un ciclo.
#el epsilon relativo de la maquina lo forza a ser cero. Mientras que el numero real menor sigue existiendo.
#a partir de ahi los dos numeros son mas pequeños de lo que la maquina lee

