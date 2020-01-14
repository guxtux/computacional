import numpy
import matplotlib.pyplot as plt
A = [2,-20,70,100,48]
X = numpy.linspace(-4,-1,7)
i = 0
ejex=[]
ejey=[]
while i < 7:
    j=0
    res = A[j]
    while j < 4:
        j += 1
        res = res*X[i]+A[j]
    print X[i], res
    ejex.append(X[i])
    ejey.append(res)
    i += 1
plt.plot(ejex,ejey)
plt.show()