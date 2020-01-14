	program exaedo5
	dimension t(0:10000),y(0:10000)
	   n=100
	   h=0.05
	 open(1,file="exaedo5.dat",status="replace")
	     y(0)=10.0e5
	do i=0,n
	t(i)=i*h/5.0
	     y(i+1)=y(i)+h*f(y(i),t(i))
	write(1,*)t(i),y(i)
	end do  
	end program  
	function f(y,t)
!	constante de decaimiento=a1
	     a1=0.1044
	     f=-a1*y
	end function f
