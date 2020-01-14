
program gaussjordan
integer:: i,j,k,n
real:: z, aux2, aux
real,allocatable :: a(:,:),x(:),p(:)!se definen las variables auxiliares para el pivoteo
write(*,*)"gauss jordan "

write(*,*)"numero de variables: "
read(*,*)n
allocate (a(n+1,n),x(n),p(n+1))
do i=1,n,1

do j=1,n+1,1 !en este do se empieza la recoleccion de los datos de la matriz
write(*,*)'a(', i,',', j,'):'
read(*,*)a(j,i)
end do
end do
do j=1,n-1,1!aqui empieza el metodo de gaussjordan
aux=a(j,j)
do k=1,n+1,1

p(k)=a(k,j)/aux
end do
do i=j+1,n,1
aux2=a(j,i)
do k=1,n+1,1
a(k,i)=a(k,i)-p(k)*aux2
end do

end do
end do
do i=1,n,1
x(i)=0

end do
x(n)=a(n+1,n)/a(n,n)
do i=n-1,1,-1
z=0;
do k=1,n,1
z=z+x(k)*a(k,i)

end do
x(i)=(a(n+1,i)-z)/a(i,i)
end do
write(*,*)'xs'
do i=1,n,1 ! en este do se imprime la solucion encontrada por el metodo de gausjordan
write(*,*)"x",i,"=",x(i)
end do
end program gaussjordan



