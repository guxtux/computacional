        program fibo
       dimension l(0:10000),g(0:10000)
!         n=8
        p=sqrt(5.0)
        write(*,*)"dame n"
        read(*,*)n
        open(1,file="fibo.dat",status="replace")
        l(1)=1
        l(2)=1
        do i=3,n
        l(i)=l(i-1)+l(i-2)              
         g(i)=(1/p)*((.5*(1.0+p))**i-(.5*(1-p))**i)
        write(1,*)l(i),g(i)
!        print*,l(i),g(i)
        end do
        print*,"revisa fibo.dat"
        end program

