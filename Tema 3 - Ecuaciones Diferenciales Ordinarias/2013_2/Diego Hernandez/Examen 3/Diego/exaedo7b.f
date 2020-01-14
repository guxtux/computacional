	program exaedo7b
	dimension t(0:10000),y(0:10000),z(0:10000)
	dimension w1(0:10000),w2(0:10000)
	dimension x1(0:10000),x2(0:10000)
	   n=200
	   h=.10
	 open(1,file="exaedo7b.dat",status="replace")
	y(0)=10
	z(0)=0.0
	     a1=1.0/2.0
	     a2=2.0/50.0
	     a3=3.0/20.0
	     a4=2.0/20.0
	do i=0,n
	t(i)=h*i
	 w1(i)=h*f1(y(i),z(i),t(i))
	 x1(i)=h*f2(y(i),z(i),t(i))
	 w2(i)=h*f1(y(i)+w1(i),z(i)+x1(i),t(i+1))
	 x2(i)=h*f2(y(i)+w1(i),z(i)+x1(i),t(i+1))
	y(i+1)=y(i)+a1*(w1(i)+w2(i))
	z(i+1)=z(i)+a1*(x1(i)+x2(i))
	write(1,*)t(i),y(i),z(i)
	 if  (abs(a4*y(i)-a3*z(i))<0.001) then 
	print*,"el maximo es"
	print*,z(i)
	print*,"y se alcansa en "
	print*,t(i)
	 end if
	end do 
	end program
	function f1(y,z,t)
	     a2=2.0/50.0
	     f1=-a2*y
	end function f1
	function f2(y,z,t)
	     a3=3.0/20
	     a4=2.0/20.0
	     f2=-a3*z+a4*y
	end function f2
