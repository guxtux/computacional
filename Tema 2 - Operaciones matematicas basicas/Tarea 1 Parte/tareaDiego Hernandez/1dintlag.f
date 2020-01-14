	program dintlag
	dimension x(0:10000), fx(0:10000), y(0:10000)
!	open(1,file="datos.dat",status="old")
!	do i=1,n
!	read(1,*)x(i),fx(i)
!	end do 
	open(2,file="problema1.dat",status="replace")
	x(1)=0
	x(2)=3
	x(3)=6
	 fx(1)=1.225
	 fx(2)=0.905
	 fx(3)=0.652
	do k=1,1000
	h=6.0/1000
	y(k)=k*h
!	print*,y(k)
	p=0
	do i=1,3
	z=fx(i)
	do j=1,3
	if(i.ne.j) z=z*(y(k)-x(j))/(x(i)-x(j))
	continue
	end do 
	p=z+p
	end do 
	write(2,*)y(k),p
	end do 
	end program
