	program motos
	dimension t(0:1000000),xt(0:1000000), yt(0:1000000)
	  n=100
	  H=1.0
	  d=30017.92
	  e=.223
	  
	  l=4395.1629
	  p=448.0288  
	  open (1,file="moto2.dat",status="new")
	  write(*,*)"dame el angulo"
	  read(*,*)theta
	  do i=0,n
	  t(i)=i*H
	  xt(i)=-d*cos(theta)*exp(-e*t)+d*cos(theta)
	  yt(i)=-l*(t-p*exp(-e*t)) +d*exp(-e*t)*sin(theta)
	  write( 1,*) t(i),xt(i),yt(i)  
	  end do
	end program
		




                                                                               
                 
