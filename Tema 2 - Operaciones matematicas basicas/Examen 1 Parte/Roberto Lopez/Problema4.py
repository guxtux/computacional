from numpy import *
from neville import *
xd=array([0.0,21.1,37.8,54.4,71.1,87.8,100.0])
yd=array([1.79,1.13,0.696,0.519,0.338,0.321,0.296])
x0=[10.0,30.0,60.0,90.0]
for k in x0:
    print 'Utiizando el metodo de Neville P(',k,')=',neville(xd,yd,k)
