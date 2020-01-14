def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*fact(x-1)
        
def expneg(x):
    i = 0.0
    resultado = 0
    while i < 100:
        resultado = resultado + (pow(-x,i)/fact(i))
        i += 1.0
    return resultado
    
def exp(x):
    i = 0.0
    resultado = 0
    while i < 100:
        resultado = resultado + (pow(x,i)/fact(i))
        i += 1.0
    return resultado
    
x=0.1
while x<=1000:
    print x, '\t', expneg(x), '\t', 1.0/exp(x)
    x *= 10
    
i=0
while i < 11:
    print fact(i)
    i += 1