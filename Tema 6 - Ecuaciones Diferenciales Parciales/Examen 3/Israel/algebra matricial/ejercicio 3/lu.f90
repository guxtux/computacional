program descomposicion 
implicit none
real, dimension(3,3):: l,u,a,b,ll,uu,r
integer i,j,k,f,g,h,v


data (a(1,i),i=1,3)/2, -1, 0/
data (a(2,i),i=1,3)/-1, 2,-1/
data (a(3,i),i=1,3)/0, -1, 2/

data (b(1,i),i=1,3)/2, -1, 0/
data (b(2,i),i=1,3)/-3, 4,-1/
data (b(3,i),i=1,3)/0, -1, 2/
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
write(*,*) '+++++++++++++++ matriz 1 ejercicio 3+++++++++++++++++++'
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
write(*,*) '++++++++++++++++multiplicacion de las matrices anteriores LU+++++++++++++++++'



DO f=1,3
DO g=1,3
R(f,g) = 0.
DO h=1,3
R(f,g) = R(f,g) + l(f,h)*u(h,g)
END DO
END DO
END DO
print*,"la matriz es:"
do v=1,3
print*,(r(v,g),g=1,3)
end do
print*
print*
print*
!+++++++++++++algoritmo de LU
ll(1,1)=b(1,1)
ll(2,1)=b(2,1)
ll(3,1)=b(3,1)
ll(1,2)=0.0
uu(1,2)=b(1,2)/ll(1,1)
ll(2,2)=b(2,2)-ll(2,1)*uu(1,2)
ll(3,2)=b(3,2)-ll(3,1)*uu(1,2)
uu(1,3)=b(1,3)/ll(1,1)
uu(2,3)=(b(2,3)-ll(2,1)*uu(1,3))/ll(2,2)
ll(3,3)=b(3,3)-ll(3,1)*uu(1,3)-ll(3,2)*uu(2,3)
ll(1,3)=0.0
ll(2,3)=0.0
uu(1,1)=1.
uu(2,2)=1.
uu(3,3)=1.
uu(2,1)=0.
uu(3,1)=0.
uu(3,2)=0.
write(*,*) '+++++++++++++++ matriz 2 ejercicio 3+++++++++++++++++++'
write(*,*) '+++++++++++++++++++++ matriz L+++++++++++++++++++'
              do i= 1,3
                    print*,(ll(i,j),j=1,3)
                           end do
print* 
print*

write(*,*) '+++++++++++++++++++++ matriz u+++++++++++++++++++'
               do i= 1,3
                   print*,(uu(i,j),j=1,3)
                         end do
write(*,*) '++++++++++++++++multiplicacion de las matrices anteriores LU+++++++++++++++++'

DO f=1,3
DO g=1,3
R(f,g) = 0.
DO h=1,3
R(f,g) = R(f,g) + ll(f,h)*uu(h,g)
END DO
END DO
END DO
print*,"la matriz es:"
do v=1,3
print*,(r(v,g),g=1,3)
end do
end program descomposicion
