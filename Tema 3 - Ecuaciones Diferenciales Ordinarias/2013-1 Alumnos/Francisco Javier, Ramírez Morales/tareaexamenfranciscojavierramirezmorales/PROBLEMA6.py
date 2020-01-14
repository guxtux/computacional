from pylab import*

# integraremos la sigiente funcion f(x)=(1/3)(x**(4/3)+1)**-1 utilizando
# la regla del trapecio para n=5
N=5
a=0.0
b=1.0
h=(b-a)/N
I=0.24375# este es el valor exacto a comparar

# ahora obtenemos  los coeficientes xi

xi=[]
x=0
xi.append(0.0)# este es  valor a
while x<b:
    x=x+h
    xi.append(x)

def f(x):
    return  (1.0/3)*(1.0/(x**(4.0/3)+1.0)) # es la funcion que queremos integrar

# obtenemos el valor de la funcion en cada uno de los puntos  xi
fi=[]
for z in xi:
    c=f(z)
    fi.append(c)

# LA REGLA ES Ii=[f(x(i))+f(x(i+1))]*h/2 y la integral es la suma de todas las Ii
i0=[]
p=len(fi)-1
j=0
for i in range(p):
     j=fi[i]+fi[i+1]
     i0.append(j)
w=sum(i0) 


I0=w*(h/2.0) #El valor de la integral
E=(abs(I-I0)/I)*100

print ' el valor de la integral es : %f5' %(I0)
print ' el error relativo es : %f5' %E

