#encoding utf-8
import math
def factorial(n):
n=0.
result= 1
e=0.
while n <= 1000:
#	  result = 1
        for i in xrange(1,n+1):
            result *=i
        e = e + (1/(factorial(result))
        result = result + 1.
	return result
        print e

        



