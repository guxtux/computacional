	program exaedo7
	dimension t(0:10000),y(0:10000)
	dimension w1(0:10000),w2(0:10000)
	   n=1000
	   h=1.0
	 open(1,file="exaedo7.dat",status="replace")
	y(0)=10
	     a1=1.0/2.0
	do i=0,n
	t(i)=h*i
	 w1(i)=h*f(y(i),t(i))
	 w2(i)=h*f(y(i)+w1(i),t(i+1))
	y(i+1)=y(i)+a1*(w1(i)+w2(i))
	write(1,*)t(i),y(i)
	 if  (abs(1.0-y(i))<0.05) then 
	print*,"la concentracion de sal es del 10% al minuto"
	print*,t(i)
	 end if
	end do 
	end program
	function f(y,t)
	     a2=2.0/50.0
	   f=-a2*y
	end function f
