	program dintlag2
        dimension x(0:10000), fx(0:10000)
       open(1,file="datos3.dat",status="old")
       do i=1,6
       read(1,*)x(i),fx(i)
       end do 
        y=200
        p=0
        do i=1,6
        z=fx(i)
        do j=1,6
        if(i.ne.j) z=z*(y-x(j))/(x(i)-x(j))
        continue
	end do
        p=z+p
        end do
	print*,y,p
        end program
















