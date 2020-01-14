PROGRAM LU4
Dimension A(10,10)
Dimension B(10)
N=4
DATA (A(1,j),j=1,4)/9,4.5,6.3,0/
DATA (A(2,j),j=1,4)/4.5,2.85,3.15,-1.54/
DATA (A(3,j),j=1,4)/6.3,3.15,5,0/
DATA (A(4,j), j=1,4) /0,-1.54,0,5/
DATA (B(j),j=1,4)/20.9,11.1,16.52,-0.4/
CALL LU(N,A,B) !CALL THE ROUTINE AND OBTAIN RESULT FROM OUTPUT FILE.

END PROGRAM LU4

SUBROUTINE LU(N,A,B)



INTEGER,INTENT(IN)::N

REAL,INTENT(INOUT)::A(10,10),B(10) 



REAL::L(10,10),U(10,10),X(10),Y(10)

DO K=1,N-1

   DO M=K+1,N

      A(M,K)=A(M,K)/A(K,K) 

   END DO

   DO I=k+1,N

     	DO J=k+1,N

         A(I,J)=A(I,J)-A(I,K)*A(K,J) 
	END DO 
   END DO

END DO


DO I=1,N

   DO J=1,N

      IF (I==J) THEN

         L(I,J)=1 

      ELSE IF(I<J)then

         L(I,J)=0 

      ELSE

         L(I,J)=A(I,J) 
      END IF

      IF (I>J) THEN

         U(I,J)=0 

      ELSE

          U(I,J)=A(I,J) 

      END IF

   END DO

END DO


Y(1)=B(1)/L(1,1)

DO I=2,N

   S=0

   DO J=1,I-1

      S=S+L(I,J)*Y(J)

   END DO

   Y(I)=(B(I)-S)/L(I,I)

END DO


X(N)=Y(N)/U(N,N)

DO I=N-1,1,-1

   S=0

   DO J=I+1,N

      S=S+U(I,J)*X(J)

   END DO

   X(I)=(Y(I)-S)/U(I,I)

END DO

DO I=1,N

   WRITE (*,*),'X =',X(I)

END DO

END SUBROUTINE




