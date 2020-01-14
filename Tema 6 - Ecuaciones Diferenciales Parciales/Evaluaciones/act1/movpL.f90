Program Mov
real, dimension(4):: y,dydx,yResultado 

n=4 !numero de EDO

x=0.0 !paso inicial


! condiciones  iniciales
y(1) = 0.5
y(2) = 0.0
y(3) = 0.0
y(4) = 1.63
h = 1.0e-3
npasos = 20000 !numero de iteraciones

open(1,file='mas.dat',status='unknown') !abriendo archivo de datos


! ComienZo 
do i=1,npasos 
write(1,1000) y(1),y(2),y(3),y(4) !escribiendo Datos

!Subrutina "derivada" (explicacion pdf)
call derivadas(x,y,dydx)

!Subrutina "rk4" solucion de las ecuaciones
call rk4(y,dydx,n,x,h,yResultado,derivadas)
x=x+h ! incremento en la posicion

do j=1,n
y(j)=yResultado(j) !cambiando valores viejos por nuevos
end do
end do
close(1)
1000 format(4(3x,f10.4)) !formato de escritura

end program


!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
subroutine derivadas(x,y,dy)
real,dimension(4):: y, dy
r = sqrt(y(1)*y(1) + y(2)*y(2))
a = 1.0/(r**2)
dy(1)=y(3)                           ! valores establecidos en el Pdf         
dy(2)=y(4)
dy(3)=-a*(y(1)/r)
dy(4)=-a*(y(2)/r)
return
end


!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
subroutine rk4(y,dydx,n,x,h,yResultado,derivadas)
integer n
real h,x,dydx(n),y(n),yResultado(n) !definicion de los pasos y las funciones a usar
external derivadas
integer i
real h6,hh,xh,dym(50),dyt(50),yt(50)! definicion de los pasos y las funciones a usar
hh=h*0.5 ! variacion de H para cada rk
h6=h/6.  ! constante en rk4
xh=x+hh  ! tamaño del paso

!_____________________________metodo rk1

do 11 i=1,n
yt(i)=y(i)+hh*dydx(i) ! dydx es el valor de la funcion en la subrutina derivadas
11 continue

!_____________________________metodo rk2

call derivadas(xh,yt,dyt)
do 12 i=1,n
yt(i)=y(i)+hh*dyt(i) !dyt es el valor de la funcion en la subrutina derivadas
12 continue

!_____________________________metodo rk3

call derivadas(xh,yt,dym)
do 13 i=1,n
yt(i)=y(i)+h*dym(i)  !dym es el valor de la funcion en la subrutina derivadas
dym(i)=dyt(i)+dym(i)
13 continue

!_____________________________metodo rk4

call derivadas(x+h,yt,dyt)
do 14 i=1,n
yResultado(i)=y(i)+h6*(dydx(i)+dyt(i)+2.*dym(i)) ! valor de cada EDO 
14 continue
return
end

