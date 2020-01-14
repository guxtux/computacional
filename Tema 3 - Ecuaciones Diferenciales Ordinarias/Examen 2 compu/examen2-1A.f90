PROGRAM SEC
REAL*16::X,X0,X1,X2,X3
!para determinar los valores de x0 y x1 se utilizo el programa examen2-1graf.f90 que te grafica f(x) y permite realizar una estimacion de donde se puede encontrar la raiz, esto fue necesario de hacer ya que la funcion diverge fuertemente para valores menores a -1 y mayores a 1.5.
X0=-1
X1=-.1
X2=X1-(EXP(X1*X1)*LOG(X1*X1)-X1/(((EXP(X1*X1)*LOG(X1*X1)-X1)-(EXP(X0*X0)*LOG(X0*X0)-X0))/(X1-X0)))
DO WHILE (ABS((EXP(X2*X2)*LOG(X2*X2)-X2)).GT.0.0000001)
X0=X1
X1=X2
X2=X1-((EXP(X1*X1)*LOG(X1*X1)-X1)/(((EXP(X1*X1)*LOG(X1*X1)-X1)-(EXP(X0*X0)*LOG(X0*X0)-X0))/(X1-X0)))
END DO
PRINT*, 'La primera raiz obtenida es: x=', X2
X0=.1
X1=1.5
X3=X1-(EXP(X1*X1)*LOG(X1*X1)-X1/(((EXP(X1*X1)*LOG(X1*X1)-X1)-(EXP(X0*X0)*LOG(X0*X0)-X0))/(X1-X0)))
DO WHILE (ABS((EXP(X3*X3)*LOG(X3*X3)-X3)).GT.0.0000001)
X0=X1
X1=X3
X3=X1-((EXP(X1*X1)*LOG(X1*X1)-X1)/(((EXP(X1*X1)*LOG(X1*X1)-X1)-(EXP(X0*X0)*LOG(X0*X0)-X0))/(X1-X0)))
END DO
PRINT*, 'La segunda raiz obtenida es: x=', X3
PRINT*, EXP(X2*X2)*LOG(X2*X2)-X2
PRINT*, EXP(X3*X3)*LOG(X3*X3)-X3
END PROGRAM SEC

