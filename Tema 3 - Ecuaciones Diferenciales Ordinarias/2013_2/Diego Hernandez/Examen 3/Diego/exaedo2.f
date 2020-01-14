	program exaedo2
!	implicit double precision (a-h,o-z)
	dimension t(0:10000),y(0:10000),g(0:10000)
	   n=500
	   h=0.001
	 open(1,file="exaedo2.dat",status="replace")
	     y(0)=0.5
!	pi**2=g
	      pi=2.0*asin(1.0)
!	a1=radio del orificio 
             a1=0.02
             a2=0.25**2
             a3=sqrt(2.0*pi**2)
             a4=(a1*a3)/(3.0*pi*a2)
	     a5=sqrt(0.5)
	do i=0,n
	t(i)=i*h
	     g(i)=sqrt(((a5-a4*t(i))/2.0))
	     y(i+1)=y(i)+h*f(y(i),t(i))
	w=abs(g(i)-y(i))
	if   (y(i)>=0.0) then
	write(1,*)t(i),y(i),w
	end if 
	end do  
	print*,"el tiempo de vacido es de"
	print*,"0.4710 seg" 
	end program  
	function f(y,t)
!	implicit double precision (a-h,o-z)
!	pi**2=g
	     pi=2.0*asin(1.0)
!       a1=radio del orificio
	     a1=0.02
	     a2=0.25**2
	     a3=sqrt(2.0*pi**2)
	     a4=(a1*a3)/(3.0*pi*a2)
	     f=-a4*sqrt(1.0/(y**3))
	end function f
