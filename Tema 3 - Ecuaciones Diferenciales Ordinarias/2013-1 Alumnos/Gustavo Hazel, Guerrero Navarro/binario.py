# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/est5/.spyder2/.temp.py
"""
a=eval(raw_input('escriba el número:'))
aN=int(a)
aD= a - aN
aD1=aD

aL=[]
aLD=[]
n=0
m=0

while a > 0:
    r=a-2*int(a/2)
    #aL[n]=r
    a=int(a/2)
    n=n+1
    print r
    
while aD1 != 1:
    rd=int(aD*2)
    #aLD[m]=rd
    aD=aD*2 - rd
    m=m+1
    print rd
#print aL, '.', aLD    
