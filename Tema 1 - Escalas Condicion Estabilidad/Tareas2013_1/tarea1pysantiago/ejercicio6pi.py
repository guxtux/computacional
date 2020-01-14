import scipy
import math
from scipy.integrate import quad
def func(x,a,b,c):
	return a/((a-x**b)**c)
        args = (1.0,2.0,0.5)
	result = integrate.quad(func,-1.0,1.0,args)
	print "integral=",result[0]

