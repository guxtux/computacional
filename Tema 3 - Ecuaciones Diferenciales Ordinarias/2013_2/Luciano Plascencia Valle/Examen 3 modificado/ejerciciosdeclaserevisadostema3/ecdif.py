# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 18:37:00 2013
MÓDULO DE MÉTODOS DE SOLUCIÓN DE ECUACIONES DIFERENCIALES
"""
##module ecdif
from varios import *
import matplotlib.pyplot as plt

def rk(ordenRK,dy,y0,t0,tn,h,prn=0,plot=0,xlab="t",ylab="y(t)",titulo="",pltfmt=".-"):
    n=int(round((tn-t0)/h))
    Oh=h**ordenRK
    tdec=decformat(h,1); ydec=decformat(Oh)
    yDatos=[y0]; tDatos=[t0]
    y=y0; t=t0
    if prn==1: print ylab[0]+"("+xlab[0]+"="+tdec %t+") = "+ydec %y
    for i in range(1,n+1):
        if ordenRK==1:      #RK1 = Euler
            k1=h*dy(y,t)
            y=y+k1
        if ordenRK==2:      #RK2 usando Trapecio = Euler mejorado
            k1=h*dy(y,t)
            k2=h*dy(y+k1,t)
            y=y+(k1+k2)/2
        if ordenRK==3:      #RK3 usando Simpson 1/3
            k1=h*dy(y,t)
            k2=h*dy(y+k1/2,t+h/2)
            k3=h*dy(y-k1+2*k2,t+h)
            y=y+(k1+k3+4*k2)/6
        if ordenRK==4:      #RK4 usando Simpson 1/3
            k1=h*dy(y,t)
            k2=h*dy(y+k1/2,t+h/2)
            k3=h*dy(y+k2/2,t+h/2)
            k4=h*dy(y+k3,t+h)
            y=y+(k1+k4)/6+(k2+k3)/3
        if ordenRK==5:      #RK4 usando Simpson 3/8
            k1=h*dy(y,t)
            k2=h*dy(y+k1/3,t+h/3)
            k3=h*dy(y+(k1+k2)/3,t+2*h/3)
            k4=h*dy(y+k1-k2+k3,t+h)
            y=y+(k1+k4+3*(k2+k3))/8
        t=t0+i*h
        tDatos.append(t)
        yDatos.append(y)
        if prn==1: print ylab[0]+"("+xlab[0]+"="+tdec %t+") = "+ydec %y+" + O("+ydec %Oh+")"
    if plot>=1: plt.plot(tDatos,yDatos,pltfmt); plt.xlabel(xlab); plt.ylabel(ylab); plt.axhline(color="k"); plt.axvline(color="k"); plt.grid(); plt.title(titulo); plt.show()
    return np.array(yDatos)

def rk_d2f(ordenRK,d2y,dy0,y0,t0,tn,h,prn=0,plot=0,xlab="t",ylab="y(t)",titulo="",pltfmt="r.-"):
    n=int(round((tn-t0)/h))
    Oh=h**ordenRK
    tdec=decformat(h,1); ydec=decformat(Oh)
    dyDatos=[dy0]; yDatos=[y0]; tDatos=[t0]
    dy=dy0; y=y0; t=t0
    if prn==1: print ylab[0]+"("+xlab[0]+"="+tdec %t+") = "+ydec %y
    for i in range(1,n+1):
        if ordenRK==2:
            k1=h*dy
            l1=h*d2y(dy,y,t)
            k2=h*(dy+l1)
            l2=h*d2y(dy+l1,y+k1,t+h)
            y=y+(k1+k2)/2
            dy=dy+(l1+l2)/2
        if ordenRK==4:
            k1=h*dy
            l1=h*d2y(dy,y,t)
            k2=h*(dy+l1/2)
            l2=h*d2y(dy+l1/2,y+k1/2,t+h/2)
            k3=h*(dy+l2/2)
            l3=h*d2y(dy+l2/2,y+k2/2,t+h/2)
            k4=h*(dy+l3)
            l4=h*d2y(dy+l3,y+k3,t+h)
            y=y+(k1+k4)/6+(k2+k3)/3
            dy=dy+(l1+l4)/6+(l2+l3)/3
        t=t0+i*h
        tDatos.append(t)
        yDatos.append(y)
        dyDatos.append(dy)
        if prn==1: print ylab[0]+"("+xlab[0]+"="+tdec %t+") = "+ydec %y+" + O("+ydec %Oh+")"
    if plot>=1: plt.figure(); plt.plot(tDatos,yDatos,pltfmt); plt.xlabel(xlab); plt.ylabel(ylab); plt.axhline(color="k"); plt.axvline(color="k"); plt.grid(); plt.title(titulo)
    if plot==2: plt.figure(); plt.plot(tDatos,dyDatos,"b"+pltfmt[1:]); plt.xlabel(xlab); plt.ylabel("d"+ylab[0]+"/d"+xlab[0]); plt.axhline(color="k"); plt.axvline(color="k"); plt.grid(); plt.title(titulo)
    if plot>=1: plt.show()
    return yDatos

"""
#def euler(dy,y0,t0,tn,h,prn=0,plot=0,xlab="t",ylab="y(t)",titulo="",pltfmt="r.-"):
#    n=int(round((tn-t0)/h))
#    Oh=h**1
#    tdec=decformat(h,1); ydec=decformat(Oh)
#    y=y0; t=t0
#    yDatos=[y0]; tDatos=[t0]
#    if prn==1: print ylab[0]+"("+xlab[0]+"="+tdec %t+") = "+ydec %y
#    for i in range(1,n+1):
#        print i,t,y,h*dy(y,t)
#        y=y+h*dy(y,t)
#        t=t0+i*h
#        print i,t,y
#        tDatos.append(t)
#        yDatos.append(y)
#        if prn==1: print ylab[0]+"("+xlab[0]+"="+tdec %t+") = "+ydec %y+" + O("+ydec %Oh+")"
#    if plot>=1: plt.plot(tDatos,yDatos,pltfmt); plt.xlabel(xlab); plt.ylabel(ylab); plt.axhline(); plt.axvline(); plt.grid(); plt.title(titulo); plt.show()
#    return yDatos
"""