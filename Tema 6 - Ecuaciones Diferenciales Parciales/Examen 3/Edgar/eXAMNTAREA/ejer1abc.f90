{\rtf1\ansi\ansicpg1252\deff0\deflang2058{\fonttbl{\f0\fswiss\fcharset0 Arial;}{\f1\fnil\fcharset0 Courier New;}{\f2\fswiss\fprq2\fcharset0 System;}}
{\*\generator Msftedit 5.41.15.1515;}\viewkind4\uc1\pard\f0\fs20 program ejercicio4\par
\pard\sl240\slmult1 !utiliza la subrutina sgetrs (lapack) que basicamente resuelve un sistema de ecuaciones lineales, usando la factorizacion LU\par
\pard\par
\f1 DIMENSION XC(0:10), Y(0:10), GM(0:6), DES(0:10)\par
\f0\par
\par
n=6\par
\pard\sl240\slmult1\par
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
A22=XC(1)**2+XC(2)**2+XC(3)**2+XC(4)**2+XC(5)**2+XC(6)**2\par
A21=XC(1)+XC(2)+XC(3)+XC(4)+XC(5)+XC(6)\par
A11=6\par
A12= XC(1)+XC(2)+XC(3)+XC(4)+XC(5)+XC(6)\par
D= A11*A22-A12*A21\par
Z1=Y(1)+Y(2)+Y(3)+Y(4)+Y(5)+Y(6)\par
Z2=X(1)*Y(1)+X(2)*Y(2)+X(3)*Y(3)+X(4)*Y(4)+X(5)*Y(5)+X(6)*Y(6)\par
\par
\pard\f1 A = (A22*Z1-A12*Z2)/D\par
 \par
B = (A11*Z2-A21*Z1-1)/D\par
\par
\f0 CALL \f1 GUN(GM,XC,A,B)\par
\par
CALL FUN(GM,Y,DES)\par
\b\f2\par
\pard\sl240\slmult1\b0\f0\par
DO I=1, N   !LA SOLUCION\par
PRINT*, XC(I), GM(I), Y(I), DES(I)\par
END DO\par
\par
END\par
\par
\pard\f1\tab SUBROUTINE GUN(GM,XC, A, B)\par
\tab DIMENSION GM(0:6) XC(0:10) \par
\tab\par
\tab GM(1) =  B*XC(1)+A\par
\tab GM(2) =  B*XC(2)+A\par
\tab GM(3) =  B*XC(3)+A\par
\tab GM(4) =  B*XC(4)+A\par
\tab GM(5) =  B*XC(5)+A\par
\tab GM(6) =  B*XC(6)+A\par
\par
\tab RETURN\par
\tab END\par
\par
\tab SUBROUTINE FUN(GM,DES,Y)\par
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
}
 