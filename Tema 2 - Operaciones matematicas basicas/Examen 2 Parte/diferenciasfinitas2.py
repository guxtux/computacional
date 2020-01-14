## module diferenciasfinitas2

#derivacion de orden 2 para un arreglo de dos vectores
#el vector x debe estar espaciado constante x(i)-x(i+1)=a para toda i
#se toma h como la diferencia entre los puntos de los dos vectores

def derivorden2(x,fx,h):
    N=len(x)-1
    i=0
    deriv=[]
    d=(-fx[i+2]+4*fx[i+1]-3*fx[i])/(2*h) #dif por adelante o(h2)
    deriv.append(d)
    i=1
    while i<N:  #diferencia central o(h2)
        d=(fx[i+1]-fx[i-1])/(2*h)
        deriv.append(d)
        i=i+1
    d=(fx[i-2]-4*fx[i-1]+3*fx[i])/(2*h) #dif por atras o(h2)
    deriv.append(d)
    return deriv

def deriv2orden2(x,f,h):
    
    t=x
    d=(f(t+h)-2*f(t)+f(t-h))/(h*h)
    
    return d

def richardson(x1,x2,p=2):
    G=(((2**p)*x1)-x2)/((2**p)-1)
    return G
