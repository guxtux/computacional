!GAUSS PROGRAMIN FORTRAN

PROGRAM GAUSS
!IMPLICIT NONE
INTEGER:: I,J,K,N
REAL:: Z, aux2, aux
REAL,ALLOCATABLE :: A(:,:),x(:),P(:)
WRITE(*,*)"gauss jordan "

WRITE(*,*)"Numero de variables: "
READ(*,*)N
ALLOCATE (A(N+1,N),x(N),P(N+1))
DO I=1,N,1

DO J=1,N+1,1
WRITE(*,*)'A(', I,',', J,'):'
READ(*,*)A(J,I)
END DO
END DO
DO j=1,N-1,1
aux=A(j,j)
DO k=1,N+1,1

P(k)=A(k,j)/aux
END DO
DO i=j+1,N,1
aux2=A(j,i)
DO k=1,N+1,1
A(k,i)=A(k,i)-P(k)*aux2
END DO

END DO
END DO
DO I=1,N,1
x(I)=0

END DO
x(N)=A(N+1,N)/A(N,N)
DO I=N-1,1,-1
Z=0;
DO K=1,N,1
Z=Z+x(K)*A(k,I)

END DO
x(I)=(A(N+1,I)-Z)/A(I,I)
END DO
WRITE(*,*)'xS'
DO I=1,N,1
WRITE(*,*)"x",i,"=",x(i)
END DO
END PROGRAM GAUSS

