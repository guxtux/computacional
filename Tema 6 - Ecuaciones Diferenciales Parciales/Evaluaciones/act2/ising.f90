PROGRAM ising
	implicit none
	
	integer :: i,j,l,N,swt
	integer, parameter :: Nxy=25

	integer, dimension(Nxy,Nxy):: S
	real (kind=8) :: r,q,r1,r2,deltaE,beta,kT,J1,Mini,Mprom,spins,buffer
	real (kind=8) :: Eini, Eprom,Ebuffer
	integer, external :: indice
	open(unit=1,file='magneg.dat',status='replace')
	open(unit=2,file='magpos.dat',status='replace')
	open(unit=3,file='ener.dat',status='replace')
	swt=1
	N=1500000						!Numero de promedios
	

	
	J1=1.d0
	
	call random_seed

	do kT=0.2, 7.0,0.05					!Numero de pasos de temperatura
		beta=1.d0/kT
		
		Mini=0.d0
		Mprom=0.d0
		Eini=0.d0
		Eprom=0.d0
		Ebuffer=0.d0
		!Iniciando lattice
		do i=1, Nxy
			do j=1, Nxy
				!call random_number(r)
				!if(r>0.5d0) then
				!	S(i,j)=1
				!else
				!	S(i,j)=-1
				!end if
				S(i,j)=1
			end do
		end do
		do i=1, Nxy
			do j=1, Nxy
				Ebuffer=Ebuffer+float(S(i,j)*S(i,indice(j+1,Nxy)))
				Ebuffer=Ebuffer+float(S(j,i)*S(indice(j+1,Nxy),i))
				Eini=Ebuffer
				Mini=Mini+float(S(i,j))
			end do
		end do
		if(swt==1)	then
			buffer=Mini/(float(Nxy*Nxy))
			write(1,*) '0.0', buffer
			write(2,*) '0.0', buffer
			write(3,*) '0.0', -Eini/float(Nxy*Nxy)
			swt=0
		end if
		!Loop de Montecarlo
		do l=1, N
			call random_number(r1)
			call random_number(r2)
		
			i=floor(Nxy*r1)+1
			j=floor(Nxy*r2)+1
			!Calcular la diferencia del cambio
			spins=float( S(indice(i+1,Nxy),j)+S(indice(i-1,Nxy),j)&
			+S(i,indice(j+1,Nxy))+S(i,indice(j-1,Nxy)))
			deltaE=J1*(float(S(i,j))*(spins)-float(-S(i,j))*(spins))
			
			if(deltaE<0.d0) then
				Mini=Mini-float(2*S(i,j))
				Eini=Eini-deltaE
				S(i,j)=-S(i,j)
			else
				q=exp(-beta*deltaE)
				call random_number(r)
				if(r<q) then
					Mini=Mini-float(2*S(i,j))
					Eini=Eini-deltaE
					S(i,j)=-S(i,j)
				end if
			end if
			if(l>1000000) then
				Mprom=Mprom+Mini
				Eprom=Eprom+Eini
			endif
		end do
		
		Mprom=Mprom/(float(500000)*float(Nxy*Nxy))
		Eprom=Eprom/(float(500000))
		if(Mprom<0) then
			write(1,*) kT, Mprom
		else
			write(2,*) kT, Mprom
		end if
		write(3,*) kt, -Eprom/(float(Nxy*Nxy))
	end do			
END PROGRAM ising

function indice(i,j)
	integer :: i,j
	if(i>j) then
		indice=1
	else if (i<1) then
		indice=j
	else 
		indice=i
	end if	
end function indice
