	program dintlag
        dimension x(0:10000), fx(0:10000), y(0:10000)
        open(1,file="datos2.dat",status="old")
        do i=1,5
        read(1,*)x(i),fx(i)
        end do 
        open(2,file="problema2.dat",status="replace")
        do k=1,1000
        h=6.0/1000
        y(k)=-3.0+k*h
!       print*,y(k)
        p=0
        do i=1,5
        z=fx(i)
        do j=1,5
        if(i.ne.j) z=z*(y(k)-x(j))/(x(i)-x(j))
        continue
	end do
        p=z+p
        end do
        write(2,*)y(k),p
        end do
        end program













