PROGRAM SECGRAF
REAL::F,X1
INTEGER::I,N
open(12,file='secgraf.dat',status='unknown')
DO I=-2000,2000
X1=I/1000.
F=EXP(X1*X1)*LOG(X1*X1)-X1
write(12,*) X1,F
end do
END PROGRAM SECGRAF
