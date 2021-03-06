{\rtf1\ansi\ansicpg1252\deff0\deflang2058{\fonttbl{\f0\fswiss\fcharset0 Arial;}{\f1\fnil\fcharset0 Courier New;}{\f2\fswiss\fprq2\fcharset0 System;}}
{\*\generator Msftedit 5.41.15.1515;}\viewkind4\uc1\pard\f0\fs20 program ejercicio4\par
\pard\sl240\slmult1 !utiliza la subrutina sgetrs (lapack) que basicamente resuelve un sistema de ecuaciones lineales, usando la factorizacion LU\par
\pard\par
REAL, ALLOCATABLE, DIMENSION(:,:) :: A\par
REAL, ALLOCATABLE, DIMENSION(:) :: B\par
INTEGER, ALLOCATABLE, DIMENSION(:,:) :: C\par
\par
INTEGER :: i, j, n, INFO\par
\par
n=4\par
ALLOCATE(A(n,n))\par
ALLOCATE(B(n))\par
\pard\sl240\slmult1 ALLOCATE(C(n,n))\par
\par
XC(1)=.1\par
XC(2)=.2\par
XC(3)=.3\par
XC(4)=.4\par
XC(5)=.5\par
XC(6)=.6\par
XC(7)=.7\par
XC(8)=.8\par
XC(9)=.9\par
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
\tab\tab B(i) = 2.122*FM(I,2)+3.0244*FM(I,3)+3.2568*FM(I,4)+3.1399*FM(I,5)+2.8579*FM(I,6)+2.514*FM(I,7)+2.1639*FM(I,8)+1.8358*FM(I,9)\par
end DO\f0\par
\pard\sl240\slmult1\par
\par
\pard CALL \b\f2 SGETRS( n, N, 1, A, N, C, B, N, INFO )\par
\pard\sl240\slmult1\b0\f0\par
DO I=1, N   !LA SOLUCION\par
PRINT*, B(I)\par
END DO\par
\par
END\par
\par
\pard\f1\tab SUBROUTINE FUN(FM,I,XC)\par
\tab DIMENSION FM(0:6,0:10) XC(0:10)\par
\tab\par
\tab DO I=1, 6 \par
\tab FM(1,J) =  1\par
\tab FM(2,J) =  X(J)\par
\tab FM(3,J) =  SIN(3.1415*X(J))\par
\tab FM(4,J) =  SIN(2*3.1415*X(J))\par
\tab END DO\par
\tab\par
\tab RETURN\par
\tab END\par
\pard\sl240\slmult1\f0\par
}
 