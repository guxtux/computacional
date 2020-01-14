PROGRAM proyrk2
REAL *8 M   , K1, K2, L1, L2, X, Y
DATA T,V,U,H/0.0,150,150,0.001/
PRINT *
PRINT *, '   T 	     U	         V 		X		Y'
PRINT  1,T,U,V
1	FORMAT(F10.5,1P4E13.6)
!KM=K/M
!BM=B/M
!W=[(U**2)+(V**2)]**0.5

OPEN(1,FILE='problema_3a.dat',	STATUS='UNKNOWN')
DO N=1 ,20
	DO KOUNT=1,50
		T=T+H
		K1=H*0.005*(((U**2)+(V**2))**0.5)*U
		L1=H*((-9.9)-(0.005*(((U**2)+(V**2))**0.5)*V))
		k2=H*0.005*((((U+K1)**2)+((V+L1)**2))**0.5)*(U+K1)
		L2=H*((-9.9)-(0.005*((((U+K1)**2)+((V+L1)**2))**0.5)*(V+L1)))
		U=U+(K1+K2)/2
		V=V+(L1+L2)/2
		X=U*T
		Y=V*T
	END DO
	WRITE(1,*)T,U,V,X,Y
	PRINT  1,T,U,V,X,Y
END DO
CLOSE(1)
END PROGRAM proyrk2
