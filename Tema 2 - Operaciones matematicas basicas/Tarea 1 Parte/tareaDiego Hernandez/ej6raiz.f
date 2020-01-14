	program ej6raiz
        e=0.001
        write(*,*)"dame el primer punto"
        read(*,*)a
        write(*,*)"dame el segundo punto"
        read(*,*)b
        p=a+((b-a)/2.0)
        print *,abs(f4(p)),a,b,p,f4(p)
        open(1,file="bisec3.dat",status="replace")
        do while (abs(f4(p))>e)
          if(f4(a)*f4(p)<0)then
           a=a
           b=p
          else if (f4(a)*f4(p)>0)then
           a=p
           b=b
           end if
         p=a+((b-a)/2.)
         write (1,*) p, f4(p)
         end do
        print*,p,f4(p)
!       si se desea obtener las raices de g solo hay que
!       ambiar f por g 
! 	 en el codigo  
        end program
        function f2(x)
         f2=2510*log(2.8e6/(2.8e6-13.3e3*x))-9.81*x-335
        end function f2
        function f4(x)
	f4=x*((3.0-2.0*x)**2)/(1-x)**3-249.2
	end function f4 


















