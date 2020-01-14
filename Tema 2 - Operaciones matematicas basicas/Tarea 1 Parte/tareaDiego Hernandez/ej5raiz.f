	program ej5raiz
        e=0.001
        write(*,*)"dame el primer punto"
        read(*,*)a
        write(*,*)"dame el segundo punto"
        read(*,*)b
        p=a+((b-a)/2.0)
        print *,abs(f3(p)),a,b,p,f3(p)
        open(1,file="bisec2.dat",status="replace")
        do while (abs(f3(p))>e)
          if(f3(a)*f3(p)<0)then
           a=a
           b=p
          else if (f3(a)*f3(p)>0)then
           a=p
           b=b
           end if
         p=a+((b-a)/2.)
         write (1,*) p, f3(p)
         end do
        print*,p,f3(p)
!       si se desea obtener las raices de fn solo hay que
!       cambiar f por fn 
!       en el codigo  
        end program
        function f(x)
        f=x**3-10.0*x**2+5.0
        end function f
        function f2(x)
         f2=2510*log(2.8e6/(2.8e6-13.3e3*x))-9.81*x-335
        end function f2
        function f3(x)
	 f3=-8.311441*x*log((x/4.44418)**(5/2))+1000000.0
	 end function f3
	 

















