PROGRAM minimosCuadrados
! recta y=a+bx ----> y=mx+b
integer, Parameter :: L=6 ,N=3
real, dimension (L):: X,X2,Y,y1,r
real, dimension (N,N+1):: A
real, dimension (N) :: Z

open(1,file='ajuste2.dat',status='unknown')
 x=(/0.1,0.4,0.5,0.7,0.9,0.9/)
 y=(/0.61,0.92,0.99,1.52,1.47,2.03/)
X2(1:L)= X(1:L)*X(1:L)
A(1,1)= L
A(1,2)= sum (X(1:L))
A(1,3)= sum (X2(1:L))
A(2,1)= A(1,2)
A(2,2)= A(1,3)
A(2,3)= sum (X2(1:L)*X(1:L))
A(3,1)= A(1,3)
A(3,2)= A(2,3)
A(3,3)= sum (X2(1:L)*X2(1:L))
Z(1) = sum(Y(1:L))
Z(2) = sum(X(1:L)*Y(1:L))
Z(3) = sum(Y(1:L)*X2(1:L))
A(1,4) =Z(1)
A(2,4) =Z(2)
A(3,4) =Z(3)

do i=1,N
  print 15, A(i,1), A(i,2), A(i,3), '|',A(i,4)
15	FORMAT (3F8.2,x,1a,x,f8.2)
end do

 d  = A(1,1)*(A(2,2)*A(3,3)-A(3,2)*A(2,3)) &
     -A(1,2)*(A(2,1)*A(3,3)-A(3,1)*A(2,3)) &
     +A(1,3)*(A(2,1)*A(3,2)-A(3,1)*A(2,2))
 db0= z(1)*(A(2,2)*A(3,3)-A(3,2)*A(2,3)) &
     -A(1,2)*(z(2)*A(3,3)- z(3)*A(2,3)) &
     +A(1,3)*(z(2)*A(3,2)- z(3)*A(2,2))
 db1= A(1,1)*(Z(2)*A(3,3)-Z(3)*A(2,3)) &
     -Z(1)*(A(2,1)*A(3,3)-A(3,1)*A(2,3)) &
     +A(1,3)*(A(2,1)*Z(3)-A(3,1)*Z(2))
 db2= A(1,1)*(A(2,2)*Z(3)-A(3,2)*Z(2)) &
     -A(1,2)*(A(2,1)*Z(3)-A(3,1)*Z(2)) &
     +Z(1)*(A(2,1)*A(3,2)-A(3,1)*A(2,2))
 b0=db0/d
 b1=db1/d
 b2=db2/d

CALL GAUSS(N,A)

print*
PRINT*, '	SOLUCION	'
PRINT*,'----------------------------'
PRINT*,'	I	B(i)	'
PRINT*,'----------------------------'

DO i=1,N
72	FORMAT (4X,I5,1PE16.6)
  PRINT 72, i, A(i,N+1)
END DO
PRINT*,'----------------------------'
PRINT*

print*, '________________________________________'
print*, '  i	  x	  y	  y1	  r'
print*, '========================================'
do i=1,L
  y1(i)=b0+b1*x(i)+b2*x2(i)
  r(i) = y(i)-y1(i)
 print 10, i, x(i), y(i), y1(i), r(i)
 write(1,10) i, x(i), y(i), y1(i), r(i)
10	FORMAT (x,I3,5f8.2)
end do
print*, '________________________________________'

print*, 'La ecuación de la parabola ajustada es:'
print*, '				y =',b0,'+',b1,'x ','+',b2,'*x2'
close(1)
STOP
end program

! ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SUBROUTINE GAUSS(N,A)

INTEGER PV
DIMENSION A(N,N+1)

EPS =1.0
10    IF (1.0 + EPS .GT. 1.0) THEN
	EPS = EPS/2.0
	GOTO 10
      END IF
eps=2*eps
! print*, 'epsilon de la maquina =', eps
eps2=2*eps
det = 1.0	!se inicializa el determinante

  DO 1010 i=1,N-1
    PV=i
    DO J=I+1,N
      IF (ABS(A(PV,I)) .LT. ABS(A(j,i))) PV=J
    END DO
      IF (PV.EQ.I) GOTO 1050
    DO JC=1,N+1
      TM =A(i,jc)
      A(i,jc) = A(PV,JC)
      A(pv,jc) = TM
    END DO
1045	DET = -1*DET	!Cada vez que se hace un pivoteo cambia el signo del determinante
1050	IF (A(i,i).EQ.0) GOTO 1200	!La mat es singular si Aii=0
  DO jr=i+1,N
    IF (A(jr,i) .NE.0) THEN
      R=A(jr,i)/A(i,i)
      DO KC=i+1, N+1
	TEMP = A(jr,kc)
	A(jr,kc) = A(jr,kc)-R*A(i,kc)
	IF (ABS(A(jr,kc)).LT.EPS2*TEMP) A(jr,kc)=0.0
      END DO
    END IF
  END DO
1010 CONTINUE
  
DO i=1,N
DET = DET*a(i,i)
END DO

PRINT*
! PRINT *, 'Determinante =', DET
PRINT*

IF (A(n,n).EQ.0) GOTO 1200
  A(N,N+1) = A(N,N+1)/A(N,N)
! Comienza la sustitucion hacia atras

DO NV=N-1, 1,-1
    VA=A(nv,N+1)
    DO K=NV+1,N
      VA = VA-A(NV,K)*A(K,N+1)
    END DO
  A(nv,n+1) = VA/a(nv,nv)
end do
RETURN
1200	PRINT*, 'LA MATRIZ ES SINGULAR'
END