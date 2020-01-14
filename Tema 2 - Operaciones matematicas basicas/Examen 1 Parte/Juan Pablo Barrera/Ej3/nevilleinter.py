##module nevilleinter

def neville(xdatos,ydatos,x):
    m=len(xdatos)
    y=ydatos
    for k in range (1,m):
        for i in range(m-k):
            y[i]=((x-xdatos[i+k])*y[i]+(xdatos[i]-x)*y[i+1])/(xdatos[i]-xdatos[i+k])
            #  \esta diagonal divide lineas de codigo
        #y[0:m-k]=((x-xdatos[k:m]*y[0:m-k]+(xdatos[0:m-k]-x)*y[1:m-k+1])/(xdatos[0:m-k]-xdatos[k:m])
    return y[0]

