PROGRAM minimosCuadrados
! recta y=a+bx ----> y=mx+b
integer, Parameter :: L=6
real, dimension (L):: X,Y,y1,r
real, dimension (2,2):: A
real, dimension (2) :: Z
real ::m

open(1,file='ajuste.dat',status='unknown')
 x=(/0.1,0.4,0.5,0.7,0.9,0.9/)
 y=(/0.61,0.92,0.99,1.52,1.47,2.03/)

A(1,1)= L
A(1,2)= sum (X(1:L))
A(2,1)= sum (X(1:L))
A(2,2)= sum (X(1:L)*X(1:L))

Z(1) = sum(Y(1:L))
Z(2) = sum(X(1:L)*Y(1:L))
 
d=A(1,1)*A(2,2)-A(1,2)*A(2,1)
db=A(2,2)*Z(1)-A(1,2)*Z(2)	!ordenada al origen
dm=A(1,1)*Z(2)-A(2,1)*Z(1)	!pendiente
b=db/d
m=dm/d

  print *, A,z
  print *, d,db,dm,b,m
print*, '________________________________________'
print*, '  i	  x	  y	  y1	  r'
print*, '________________________________________'
do i=1,L
  y1(i)=m*x(i)+b
  r(i) = y(i)-y1(i)
 print 10, i, x(i), y(i), y1(i), r(i)
 write(1,10) i, x(i), y(i), y1(i), r(i)
10	FORMAT (x,I3,5f8.2)
end do
print*, '________________________________________'

print*, 'La ecuación de la recta ajustada es:'
print*, '				y =',m,'x ','+',b
close(1)
end program

