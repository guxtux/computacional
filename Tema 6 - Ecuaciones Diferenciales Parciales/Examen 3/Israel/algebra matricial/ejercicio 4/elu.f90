program descomposicion 
implicit none
real, dimension(3,3):: l,u,a
real, dimension(3)::b, y, x
integer i,j,k,f,g,h,v


data (a(1,i),i=1,3)/2, -1, 0/
data (a(2,i),i=1,3)/-1, 2,-1/
data (a(3,i),i=1,3)/0, -1, 2/
data (b(i),i=1,3)/1, 2, 3/

!+++++++++++++algoritmo de LU
l(1,1)=a(1,1)
l(2,1)=a(2,1)
l(3,1)=a(3,1)
l(1,2)=0.0
u(1,2)=a(1,2)/l(1,1)
l(2,2)=a(2,2)-l(2,1)*u(1,2)
l(3,2)=a(3,2)-l(3,1)*u(1,2)
u(1,3)=a(1,3)/l(1,1)
u(2,3)=(a(2,3)-l(2,1)*u(1,3))/l(2,2)
l(3,3)=a(3,3)-l(3,1)*u(1,3)-l(3,2)*u(2,3)
l(1,3)=0.0
l(2,3)=0.0
u(1,1)=1.
u(2,2)=1.
u(3,3)=1.
u(2,1)=0.
u(3,1)=0.
u(3,2)=0.
write(*,*) '+++++++++++++++ ejercicio 4+++++++++++++++++'
write(*,*) '+++++++++++++++++++++ matriz L+++++++++++++++++++'
              do i= 1,3
                    print*,(l(i,j),j=1,3)
                           end do
print* 
print*

write(*,*) '+++++++++++++++++++++ matriz u+++++++++++++++++++'
               do i= 1,3
                   print*,(u(i,j),j=1,3)
                         end do

!algoritmo de las soluciones

y(1)=b(1)/l(1,1)
y(2)=(b(2)-l(2,1)*y(1))/l(2,2)
y(3)=(b(3)-l(3,1)*y(1)-l(3,2)*y(2))/l(3,3)

x(3)=y(3)
x(2)=(y(2)-u(2,3)*x(3))
x(1)=y(1)-u(1,2)*x(2)-u(1,3)*x(3)

print*
print*
print*
print*

write(*,*) 'las soluciones son: x1',x(1),'x2',x(2),'x3',x(3)

end program 

