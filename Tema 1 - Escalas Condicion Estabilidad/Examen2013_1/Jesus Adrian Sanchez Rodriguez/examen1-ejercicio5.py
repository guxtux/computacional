def fibo(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fibo(i-1)+fibo(i-2)
        
def fibo2(i):
    return 5.0**(-0.5) * ((0.5*(1+5.0**0.5))**i - (0.5*(1-5.0**0.5))**i)
    
i = 3
while i <= 50:
    print i, '\t', fibo(i), '\t', fibo2(i)
    i += 1