PROGRAM AJUSTE

DIMENSION X(0:100), Y(0:100), A(0:10, 0:10), GG(0:100)
DOUBLEPRECISION A
PRINT *
PRINT*, 'AJUSTE DE CURVA MEDIANTE MINIMOS CUADRADOS'
PRINT*

DATA IN/6/
DATA (X(J), J=1,6)/0.1, 0.4, 0.5, 0.7, 0.9, 0.9/
DATA (Y(J), J=1,6)/0.61, 0.92, 0.99, 1.52, 1.47, 2.03/

PRINT*, ' AJUSTE POLINOMIAL'
!"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PRINT*, 'DE EL ORDEN DEL POLINOMIO'

READ*, NORD
M=NORD+1
DO K=1,M
  DO J=1, M+1
    A(K,J)=0.0
  END DO
END DO

DO K=1,M   
  DO I=1,IN   !IN ES EL NUMERO DE PUNTOS DATOS
    DO J=1, M
     JJ=K-1 + J-1
     YY=1.0
     IF (JJ .NE. 0) YY=X(I)**JJ
     A(K,J)=A(K,J)+YY
    END DO
    JEX=K-1
    YY=1.0
    IF(JEX.NE. 0) YY=X(I)**JEX 
     A(K, M+1)= A(K, M+1)+Y(I)*YY
   END DO
END DO
GOTO 220

220  DO I=1, M
        PRINT 50, (A(I,J), J=1, M+1)
     END DO
50   FORMAT (1X, 1P7E11.3)
     N=M
       CALL GAUSS(M,A)
    PRINT*
    PRINT*, 'DETERMINCION DE COEFICIENTES'
    PRINT*, '____________________________________________'
      PRINT*, ' POTENCIA           COEFICIENTE'
    PRINT*,'______________________________________________'
    DO I= 1, M
       
       WRITE (6,595) I-1,A(I, M+1)
   END DO
595 FORMAT(2X, I4, 8X, F12.6)
   PRINT*, '_______________________________________________'
   PRINT*
   PRINT*
   DO I=1, IN
     GG(I)=0.0
     DO K=1,M
       
        GG(I)=GG(I)+A(K,M+1)*X(I)**(K-1)
     END DO
   END DO
   PRINT*, 'EVALUACION DE ERROR'
   PRINT*, '_________________________________________________'
   PRINT*, ' I           X(I)    Y(I)    POLINOMIO      DESVIACION '
   PRINT*, '_________________________________________________'

OPEN(9, file="datos.dat", status="unknown")

   DO I=1, IN
     WRITE (6,435)I,X(I),Y(I),GG(I),Y(I)-GG(I)
write(9,*) X(i),y(i)

   END DO
435 FORMAT(I4, 3X, F8.2, 2X, F10.5, 3X, F12.7, 2X, F11.6)
   PRINT*, '_________________________________________________'
   PRINT*
   STOP 
close (9)
   END

!"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  SUBROUTINE GAUSS(N,A)
  DOUBLEPRECISION A, TM, VA, R
  DIMENSION A(0:10,0:10)
  DO I=1, N-1
    IPV=I
    DO J=I+1, N
      IF (ABS(A(IPV,I)) .LT. ABS(A(J,I)))  IPV=J
    END DO
    IF (IPV.NE.I) THEN
      DO JC=1,N+1
         TM=A(I,JC)
         A(I,JC)=A(IPV,JC)
         A(IPV,JC)=TM
      END DO
    END IF
    DO JR=I+1,N
      IF (A(JR,I) .NE. 0) THEN
       IF (A(I,I).EQ. 0.0) GOTO 840
       R=A(JR,I)/A(I,I)
       DO KC=I+1, N+1
          A(JR, KC)=A(JR,KC)-R*A(I,KC)
       END DO
      END IF
    END DO
  END DO  

!SUSTITUCION HACIA ATRAS
  
  IF (A(N,N) .EQ. 0) GOTO 840
  A(N,N+1)=A(N,N+1)/A(N,N)
  DO NV=N-1, 1, -1
     VA=A(NV, N+1)
     DO K=NV+1, N
        VA=VA-A(NV,K)*A(K,N+1)
     END DO
     A(NV, N+1)=VA/A(NV,NV)
  END DO
  RETURN
840 PRINT *, 'LA MATRIZ ES SINGULAR'
  RETURN
  END

