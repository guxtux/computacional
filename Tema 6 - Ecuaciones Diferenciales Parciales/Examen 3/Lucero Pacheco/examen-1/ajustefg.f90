PROGRAM eliminagauss
integer, Parameter :: L=6 ,N=4
real, dimension (N,N+1):: A
DIMENSION X(L),y(L), Y1(L), r(L), B(N)

open(1,file='ajustef.dat',status='unknown')
 x=(/0.1,0.4,0.5,0.7,0.7,0.9/)
 y=(/0.61,0.92,0.99,1.52,1.47,1.03/)
A(1,1)= L
A(1,2)= sum (X(1:L))
A(1,3)= sum (sin(X(1:L)))
A(1,4)= sum (exp(x(1:L)))
A(1,5)= sum (Y(1:L))

A(2,1)= A(1,2)
A(2,2)= sum (X(1:L)*f2(x(1:L)))
A(2,3)= sum (sin(X(1:L))*f2(X(1:L)))
A(2,4)= sum (exp(X(1:L))*f2(X(1:L)))
a(2,5)= sum (Y(1:L)*f2(x(1:L)))

A(3,1)= sum (sin(X(1:L)))
A(3,2)= sum (X(1:L)*f3(X(1:L)))
A(3,3)= sum (sin(X(1:L))*f3(X(1:L)))
A(3,4)= sum (exp(X(1:L))*f3(X(1:L)))
A(3,5)= sum (Y(1:L)*f3(X(1:L)))


A(4,1)= sum (exp(X(1:L)))
A(4,2)= sum (X(1:L)*f4(X(1:L)))
A(4,3)= sum (sin(X(1:L))*f4(X(1:L)))
A(4,4)= sum (exp(2*X(1:L)))
A(4,5)= sum (Y(1:L)*f4(X(1:L)))

CALL GAUSS(N,A)

PRINT*, '	Coeficientes	'
PRINT*,'----------------------------'
PRINT*,'	I	B(i)	'
PRINT*,'============================'

DO i=1,N
72	FORMAT (4X,I5,1PE16.6)
    B(i)= A(i,N+1)
  PRINT 72, i, B(i)

END DO
PRINT*,'----------------------------'
PRINT*
print*, '________________________________________'
print*, '  i	  x	  y	  y1	  r'
print*, '========================================'

do i=1,L
  y1(i)=b(1)+b(2)*x(i)+b(3)*sin(x(i))+b(4)*exp(x(i))
  r(i) = y(i)-y1(i)
 print 10, i, x(i), y(i), y1(i), r(i)
 write(1,10) i, x(i), y(i), y1(i), r(i)
10	FORMAT (x,I3,5f8.2)
end do
print*, '________________________________________'

print*, 'La ecuación de la funcion ajustada es:'
print 22, 'y =',b(1),'+',b(2),'*x +',b(3),'*sin(x) + ',b(4),'*exp(x)'
22	FORMAT(20X,A3,F8.2,A3,F8.2,A5,F8.2,A10,F8.2,A7)
close(1)
stop

END PROGRAM

! ++++++++++++++++++++++++++++++++++++++
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

! PRINT*
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


function f1(x)
f1=1
end function
function f2(x)
f2=x
end function
function f3(x)
f3=sin(x)
end function
function f4(x)
f4=exp(x)
end function
