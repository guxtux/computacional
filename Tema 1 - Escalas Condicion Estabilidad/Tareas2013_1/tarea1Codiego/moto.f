	program moto
	dimension t(10000),xt(10000), yt(10000)
	  n=100 
	  H=1.0/100.0
	  d=30017.92
	  e=.00223
	  f=33500.0
	  l=4395.1629
	  p=448.0288
	  do j=1,90,10 
	  open (j,file="moto.dat",status="new")
	  the=j
	  do i=0,n
	  t(i)=i*H
	  xt(i)=-d*cos(the)*exp(-e*t)+d*cos(the) 
	  yt(i)=-l*(t-p*exp(-e*t)) +d*exp(-e*t)*sin(the)
	  write( j,*) t(i),xt(i),yt(i)
	  end do 
	  end do 
	end program 
