from scipy import*
from scipy.integrate import romberg
u=arange(0.05,1.05,0.05)
p=u**3
t=1/u

    
def f0(x): return  p[0]*((x**4.0/(exp(x)-1.0))+x**4)
def f1(x): return  p[1]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f2(x): return  p[2]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f3(x): return  p[3]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f4(x): return  p[4]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f5(x): return  p[5]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f6(x): return  p[6]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f7(x): return  p[7]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f8(x): return  p[8]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f9(x): return  p[9]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f10(x): return  p[10]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f11(x): return  p[11]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f12(x): return  p[12]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f13(x): return  p[13]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f14(x): return  p[14]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f15(x): return  p[15]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f16(x): return  p[16]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f17(x): return  p[17]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f18(x): return  p[18]*(x**4.0)*(exp(x))/(exp(x)-1.0)
def f19(x): return  p[19]*(x**4.0)*(exp(x))/(exp(x)-1.0)


R=[]
r0=romberg(f0,0,t[0],show=False)
r1=romberg(f1,0,t[1],show=False)
r2=romberg(f2,0,t[2],show=False)
r3=romberg(f3,0,t[3],show=False)
r4=romberg(f4,0,t[4],show=False)
r5=romberg(f5,0,t[5],show=False)
r6=romberg(f6,0,t[6],show=False)
r7=romberg(f7,0,t[7],show=False)
r8=romberg(f8,0,t[8],show=False)
r9=romberg(f9,0,t[9],show=False)
r10=romberg(f10,0,t[10],show=False)
r11=romberg(f11,0,t[11],show=False)
r12=romberg(f12,0,t[12],show=False)
r13=romberg(f13,0,t[13],show=False)
r14=romberg(f14,0,t[14],show=False)
r15=romberg(f15,0,t[15],show=False)
r16=romberg(f16,0,t[16],show=False)
r17=romberg(f17,0,t[17],show=False)
r18=romberg(f18,0,t[18],show=False)
r19=romberg(f19,0,t[19],show=False)

print r0,r1,r2
                           

                      
                  
                  
