f0 = 0.431711
f1 = 0.398519
f2 = 0.367879
f3 = 0.339596
f4 = 0.312486
h = 0.08

df = (f3-f1)/(2*h)

d2f = (f3 - 2*f2 + f1)/(h**2)
print "la primera derivada en el punto 1.0 es df(1.0)/dx = " ,df,

print "la segunda derivada en el punto 1.0 es d2f(1.0)/dx2 = " ,d2f,
