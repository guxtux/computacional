#encoding: utf-8
import math
N=input("Ingrese un número:")
n=1.
f=0.
while n <= N:
	f= (1/(1-math.tanh(n)))
	n = n + 1
	print f

