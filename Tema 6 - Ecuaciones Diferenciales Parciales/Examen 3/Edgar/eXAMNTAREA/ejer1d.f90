{\rtf1\ansi\ansicpg1252\deff0\deflang2058{\fonttbl{\f0\fswiss\fcharset0 Arial;}{\f1\fnil\fcharset0 Courier New;}{\f2\fswiss\fprq2\fcharset0 System;}}
{\*\generator Msftedit 5.41.15.1515;}\viewkind4\uc1\pard\f0\fs20 program ejercicio4\par
\pard\sl240\slmult1 !utiliza la subrutina sgetrs (lapack) que basicamente resuelve un sistema de ecuaciones lineales, usando la factorizacion LU\par
\pard\f1 DIMENSION xc(0:10), GM(0:10), FM(0:6,0:10), Y(0:10)\par
\f0\par
REAL, ALLOCATABLE, DIMENSION(:,:) :: A\par
REAL, ALLOCATABLE, DIMENSION(:) :: B\par
INTEGER, ALLOCATABLE, DIMENSION(:,:) :: C\par
\par
INTEGER :: i, j, n, INFO\par
\par
n=3\par
ALLOCATE(A(n,n))\par
ALLOCATE(B(n))\par
\pard\sl240\slmult1 ALLOCATE(C(n,n))\par
\par
XC(1)=.1\par
XC(2)=.4\par
XC(3)=.5\par
XC(4)=.7\par
XC(5)=.9\par
XC(6)=.9\par
\par
Y(1)=.61\par
Y(2)=.92\par
Y(3)=.99\par
Y(4)=1.52\par
Y(5)=1.47\par
Y(6)=2.03\par
\par
\f1 CALL FUN(FM,I,X)\f0\par
\par
\pard\f1 do j=1, N\par
\tab do I=1,N\par
\tab\tab A(i,j) = FM(I,1)*FM(J,1)+FM(I,2)*FM(J,2)+FM(I,3)*FM(J,3)+FM(I,4)*FM(J,4)+FM(I,5)*FM(J,5)+FM(I,6)*FM(J,6)\par
\tab end DO\par
\pard\sl240\slmult1 end DO\f0\par
\par
\pard\f1 do I=1,N\par
\tab\tab B(i) = .61*FM(I,1)+.92*FM(I,2)+.99*FM(I,3)+1.52*FM(I,4)+1.47*FM(I,5)+2.03*FM(I,6)\par
end DO\f0\par
\pard\sl240\slmult1\par
\par
\pard CALL \b\f2 SGETRS( n, N, 1, A, N, C, B, N, INFO )\par
\pard\sl240\slmult1\b0\f0\par
DO I=1, N   !LA SOLUCION DEL SISTEMA\par
PRINT*, B(I)\par
END DO\par
\par
\pard\f1 CALL GUN(GM,XC,B)\par
\pard\sl240\slmult1\f0 CALL \f1 FUNC(GM,Y,DES)\par
\f0\par
DO I=1, 6   !LA SOLUCION\par
PRINT*, XC(I), GM(I), Y(I), DES(I)\par
END DO\par
\par
\par
\par
END\par
\par
\pard\f1\tab SUBROUTINE FUN(FM,I,XC)\par
\tab DIMENSION FM(0:6,0:10) XC(0:10)\par
\tab\par
\tab DO I=1, 6 \par
\tab FM(1,J) =  1\par
\tab FM(2,J) =  X(J)\par
\tab FM(3,J) =  X(J)*X(J)\par
\tab END DO\par
\tab\par
\tab RETURN\par
\tab END\par
\par
\tab SUBROUTINE GUN(GM,XC,B)\par
\tab DIMENSION GM(0:6) XC(0:10) B(0:3)\par
\tab\par
\tab GM(1) =  B(3)*XC(1)*XC(1)+B(2)*XC(1)+B(1)\par
\tab GM(2) =  B(3)*XC(2)*XC(2)+B(2)*XC(2)+B(1)\par
\tab GM(3) =  B(3)*XC(3)*XC(3)+B(2)*XC(3)+B(1)\par
\tab GM(4) =  B(3)*XC(4)*XC(4)+B(2)*XC(4)+B(1)\par
\tab GM(5) =  B(3)*XC(5)*XC(5)+B(2)*XC(5)+B(1)\par
\tab GM(6) =  B(3)*XC(6)*XC(6)+B(2)*XC(6)+B(1)\par
\par
\tab RETURN\par
\tab END\par
\tab\par
\tab SUBROUTINE FUNC(GM,Y,DES)\par
\tab DIMENSION GM(0:6) Y(0:10) DES(0:10) \par
\tab\par
\pard\sl240\slmult1\tab DES(1)=Y(1)-GM(1)\par
\tab DES(2)=Y(2)-GM(2)\par
\tab DES(3)=Y(3)-GM(3)\par
\tab DES(4)=Y(4)-GM(4)\par
\tab DES(5)=Y(5)-GM(5)\par
\tab DES(6)=Y(6)-GM(6)\par
\pard\par
\tab RETURN\par
\tab END\par
\pard\sl240\slmult1\f0\par
\par
}
 