program matriz
implicit none
integer,dimension(10,10)::t
integer,dimension(10,10)::m
integer,dimension(10,10)::r
integer,dimension(10,10)::c
integer,dimension(10,10)::d
integer:: i,j,k,n,g

data (m(1,i), i=1,3)/1,2,3 /
data (m(2,i), i=1,3)/0,1,4 /
data (m(3,i), i=1,3)/3,0,2/
data (t(1,i), i=1,3)/4,1,3 /
data (t(2,i), i=1,3)/3,2,1 /
data (t(3,i), i=1,3)/0,1,2 /


do i=1,3
DO j=1,3
R(i,j) = 0
DO k=1,3
R(i,j) = R(i,j) + m(i,k)*t(k,j)
END DO
END DO
END DO
print*,"la matriz E es:"
do n=1,3
print*,(r(n,g),g=1,3)
end do
print*
print*
do i=1,3
do j=1,3
c(i,j)=m(i,j)+t(i,j)
d(i,j)=m(i,j)-t(i,j)
end do
end do


print*,"la matriz C es:"
do n=1,3
print*,(c(n,g),g=1,3)
end do
print*
print*

print*,"la matriz D es:"
do n=1,3
print*,(d(n,g),g=1,3)
end do
end program matriz
