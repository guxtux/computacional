PROGRAM exatreseje2b

   INTEGER::i,j,det,N,efe
   REAL:: gx,ri,efe1
   DIMENSION A(10,11)
   DIMENSION B(10,11)
   DIMENSION X(10)
   OPEN (19,FILE='exatreseje2bi.dat' , STATUS='UNKNOWN')
             N=4
	DATA M /9/

	DATA (A(1,J), J=1,2) /0.1, 0.0    /
	DATA (A(2,J), J=1,2) /0.2, 2.1220 /
	DATA (A(3,J), J=1,2) /0.3, 3.0244 /
	DATA (A(4,J), J=1,2) /0.4, 3.2568 /
	DATA (A(5,J), J=1,2) /0.5, 3.1399 /
	DATA (A(6,J), J=1,2) /0.6, 2.8579 /
	DATA (A(7,J), J=1,2) /0.7, 2.5140 /
	DATA (A(8,J), J=1,2) /0.8, 2.1639 /
	DATA (A(9,J), J=1,2) /0.9, 1.8358 /
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     M=9
     B(1,1)=0
          DO i=1,M
              B(1,1)=B(1,1)+ (  (FUN1( A(i,1)  )) * (FUN1(A(i,1))  ))
          END DO       
     B(1,2)=0
          DO i=1,M
              B(1,2)=B(1,2)+( (FUN2( A(i,1)  )) * (FUN1(A(i,1))  ))
          END DO         
      
     B(1,3)=0
          DO i=1,M
              B(1,3)=B(1,3)+( (FUN3( A(i,1)  )) * (FUN1(A(i,1))  ))
          END DO

     B(1,4)=0
          DO i=1,M
              B(1,4)=B(1,4)+( (FUN4( A(i,1)  )) * (FUN1(A(i,1))  ))
          END DO

     B(1,5)=0
          DO i=1,M
              B(1,5)=B(1,5)+((A(i,2)*FUN1(A(i,1))))
          END DO
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      B(2,1)=B(1,2)

      B(2,2)=0
           DO i=1,M
               B(2,2)=B(2,2)+( (FUN2( A(i,1)  )) * (FUN2(A(i,1))  ))
           END DO

      B(2,3)=0
            DO i=1,M
              B(2,3)=B(2,3)+( (FUN3( A(i,1)  )) * (FUN2(A(i,1))  ))
            END DO

      B(2,4)=0
          DO i=1,M
              B(2,4)=B(2,4)+( (FUN4( A(i,1)  )) * (FUN2(A(i,1))  ))
          END DO

      B(2,5)=0
          DO i=1,M
              B(2,5)=B(2,5)+((A(i,2)*FUN2(A(i,1))))
          END DO
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      B(3,1)=B(1,3)

      B(3,2)=0
           DO i=1,M
               B(3,2)=B(3,2)+( (FUN2( A(i,1)  )) * (FUN3(A(i,1))  ))
           END DO

      B(3,3)=0
            DO i=1,M
              B(3,3)=B(3,3)+( (FUN3( A(i,1)  )) * (FUN3(A(i,1))  ))
            END DO

      B(3,4)=0
          DO i=1,M
              B(3,4)=B(3,4)+( (FUN4( A(i,1)  )) * (FUN3(A(i,1))  ))
          END DO

      B(3,5)=0
          DO i=1,M
              B(3,5)=B(3,5)+((A(i,2)*FUN3(A(i,1))))
          END DO
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      B(4,1)=B(1,4)

      B(4,2)=0
           DO i=1,M
               B(4,2)=B(4,2)+( (FUN2( A(i,1)  )) * (FUN4(A(i,1))  ))
           END DO

      B(4,3)=0
            DO i=1,M
              B(4,3)=B(4,3)+( (FUN3( A(i,1)  )) * (FUN4(A(i,1))  ))
            END DO

      B(4,4)=0
          DO i=1,M
              B(4,4)=B(4,4)+( (FUN4( A(i,1)  )) * (FUN4(A(i,1))  ))
          END DO

      B(4,5)=0
          DO i=1,M
              B(4,5)=B(4,5)+((A(i,2)*FUN4(A(i,1))))
          END DO
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111
	PRINT *, 'Matriz aumentada'
	PRINT *

	DO I = 1, N                
		PRINT 61, (B(I,J), J=1,5)
61		FORMAT(1X,1P6E12.4)
	END DO

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   	PRINT *

	CALL GAUSS(N,B)

	PRINT *
	PRINT *, '   SOLUCION   '
	PRINT *, '--------------------------------------'
	PRINT *, '     I     X(I)     '
	PRINT *, '--------------------------------------'

	DO I=1,N
72		FORMAT(5X, I5, 1PE16.6)
                X(i)=B(I,N+1)
		PRINT 72, I, X(i)            
	END DO

	PRINT *, '--------------------------------------'
	PRINT *

	!STOP
    
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

       DO i=1,6

            gx=(   (X(1)*FUN1(A(i,1))) + ( X(2)*FUN2(A(i,1)) ) +( X(3)*FUN3(A(i,1)))+( X(4)*FUN4(A(i,1))  ) )

            ri=A(i,2)-gx

       WRITE (19,*),A(i,1),A(i,2),gx,ri,0.0

        END DO
 STOP
 END PROGRAM exatreseje2b
!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SUBROUTINE GAUSS(N,B)
	INTEGER PV,JC,I,det,efe  
	DIMENSION B(10,11)
	EPS = 1.0       

10	IF (1.0 + EPS .GT. 1.0) THEN
		EPS = EPS/2.0
		GOTO 10
	END IF
	
	EPS = EPS*2
	PRINT *, '    EPSILON DE LA MAQUINA = ', EPS

	EPS2= EPS*2

	DET = 1.0		!Se incializa el determinante

	DO 1010 I=1, N-1
		PV=I

		DO J=I+1, N
			IF (ABS(B(PV,I)) .LT. ABS(B(J,I))) PV=J
		END DO

		IF (PV .EQ. I) GOTO 1050

		DO JC=1, N+1
			TM=B(I,JC)
			B(I,JC)=B(PV,JC)
                        B(PV,JC)=TM

		END DO


1045		DET=-1*DET   !Cada vez que se hace un pivoteo, cambia el signo de DET               
                
1050		IF (B(I,I) .EQ. 0) GOTO 1200 	!La matriz es singular si B(I,I)= 0
		DO JR=I+1, N
			IF (B(JR,I) .NE. 0) THEN
				R=B(JR,I)/B(I,I)
				DO KC=I+1, N+1
					TEMP=B(JR,KC)
					B(JR,KC)=B(JR,KC)-R*B(I,KC)
					IF (ABS(B(JR,KC)) .LT. EPS2*TEMP) B(JR,KC)=0.0
!Si el resultado de la resta es menor que el doble del epsilon de la maquina por el
!valor original, se deja el valor de cero.
				END DO
			END IF
		END DO
1010	CONTINUE
        
	DO I=1, N
                !PRINT*,B(i,i)
		DET=DET*B(I,I)
	END DO

	PRINT *
	PRINT *, 'DETERMINANTE=', DET
	PRINT*

	IF (B(N,N) .EQ. 0) GOTO 1200
	B(N,N+1)=B(N,N+1)/B(N,N)

	      DO NV=N-1, 1, -1		!Comienza la sustitución hacia atrás
		VA=B(NV,N+1)

		    DO K=NV+1, N
			VA=VA-B(NV,K)*B(K,N+1)
		    END DO

	        B(NV,N+1)=VA/B(NV,NV)
              
	      END DO

	RETURN

1200	PRINT *,'LA MATRIZ ES SINGULAR'
	END

!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
FUNCTION FUN1(efe1)
FUN1=1
RETURN
END
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
FUNCTION FUN2(efe1)
FUN2=efe1
RETURN
END
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
FUNCTION FUN3(efe1)
pi=3.141592654
FUN3=SIN(efe1*pi)
RETURN
END
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
FUNCTION FUN4(efe1)
pi=3.141592654
dospi=2*pi
FUN4=SIN(efe1*dospi)
RETURN
END
!+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	
