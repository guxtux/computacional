        program ej4raiz
        e=0.001
        write(*,*)"dame el primer punto"
        read(*,*)a
        write(*,*)"dame el segundo punto"
        read(*,*)b
        p=a+((b-a)/2.0)
        print *,abs(f2(p)),a,b,p,f2(p)
        open(1,file="bisec.dat",status="replace")
        do while (abs(f2(p))>e)
          if(f2(a)*f2(p)<0)then
           a=a
           b=p
          else if (f2(a)*f2(p)>0)then
           a=p
           b=b
           end if
         p=a+((b-a)/2.)
         write (1,*) p, f2(p)
         end do
	print*,p,f2(p)
!       si se desea obtener las raices de g solo hay que
!	ambiar f por g 
!       en el codigo  
        end program
        function f(x)
        f=x**3-10.0*x**2+5.0
        end function f
        function g(x)
        g=x-tan(x)
        end function g
	function f2(x)
	 f2=2510*log(2.8e6/(2.8e6-13.3e3*x))-9.81*x-335
	end function f2
	













