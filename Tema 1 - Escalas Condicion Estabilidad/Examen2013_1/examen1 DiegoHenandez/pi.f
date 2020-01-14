        program pi
        dimension sen(0:1000)
!        n=19
        write(*,*)"dame n"
        read(*,*)n
        piex=4.0*atan(1.0)
        open(1,file="pi.dat",status="replace")
        sen(2)=1
        do i=3,n
        sen(i)=(sen(i-1))/(sqrt(2.0*(1.0+sqrt(1.0-sen(i-1)))))
        pib=(2.0**(i-1))*sen(i) 
        err=abs((piex-pib)/piex)
        write(1,*)i,sen(i),pib,err
!        print*,sen(i),pib
        end do
        print*,"revisa pi.dat" 
        end program
        
        
