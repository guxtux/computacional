PROGRAM Conicals

     !Este programa es para identificar cónicas y sus caracteristicas a 
     !partir de una ecuación del tipo: ax^2+2bxy+cy^2+2dx+2ey+f=0   
     real*8 a,b,c,d,e,f    ! Coeficientes de la ecuación.
     real*8 ex,xc,yc,la,lb,xf1,yf1,xf2,yf2,xs1,ys1,xs2,ys2,xv1,yv1,xv2,yv2
    
     !  Variables de salida:
     !  typ: tipo de conica:
     !       1: elipse
     !       2: hipérbola
     !       3: parábola
     !       4: circulo
     !       5: linea
     !       6: dos líneas
     !       7: punto
     !       8: nada, cosa rara
     !  ex: excentricidad
     !  xc,yc: coordenadas del centro
     !  la,lb: la es radio en caso de circulo y la,lb son los ejes en caso de elipse
     !  xf1,yf1,xf2,yf2: focos
     !  xs1,ys1,xs2,ys2: coordenadas de la cresta de la hiperbola
     !  xv1,yv1,xv2,yv2: Ejes     
	 

     
     real*8 delta,u,l,m,x2,y2	! Estas son variables internas
     integer typ

  print *,''
  print *,'  REDUCCIÓN DE CÓNICAS'
  print *,' ax^2+2bxy+cy^2+2dx+2ey+f=0 '
  print *,''
  write(*,200,advance='no'); read *, a
  write(*,201,advance='no'); read *, b 
  write(*,202,advance='no'); read *, c
  write(*,203,advance='no'); read *, d 
  write(*,204,advance='no'); read *, e 
  write(*,205,advance='no'); read *, f
  print *,''
  b=b/2; d=d/2; e=e/2
  delta=a*c-b*b		!acá se calcula el'determinante' para elejir subrutina
  if (delta.eq.0) then
    call Parabola(a,b,c,d,e,f,typ,l,m,xc,yc,xv1,yv1,xf1,yf1,ex)
  else
    xc=(b*e-d*c)/delta
    yc=(b*d-a*e)/delta
    f = f + a*xc*xc+2*b*xc*yc+c*yc*yc+2*d*xc+2*e*yc
    if (f.eq.0) then
      if (delta>0) then
	    typ=7 
	  else 
	    typ=6  !7= degenerada en punto, 6=degenerada en dos lineas
        goto 100
      end if
    end if
    u=dsqrt((a-c)*(a-c)+4*b*b)
    l=(a+c-u)/2; m=(a+c+u)/2
    if (a.eq.c.and.b.eq.0) then
      if (f*a>=0) then
        typ=8;  ! No es conica ni degenerada, hay misero de mi.
        goto 100
      else
        typ=4   ! Circulo
        la=dsqrt(-f/a)
        ex=1.d0
        goto 100
      end if
    end if
    if (a<c.and.b.eq.0) then
      x2=1.d0; y2=0.d0; xv1=1.d0; yv1=0.d0
    else
      xv1=b; yv1=1.d0-a
      u=sqrt(xv1*xv1+yv1*yv1)
      x2=xv1/u; y2=yv1/u
    end if
    if (delta<0) then
	  call Hyperbola(a,b,c,d,e,f,typ,l,m,xc,yc,xv1,yv1,xv2,yv2,xs1,ys1,xs2,ys2, &
	                 xf1,yf1,xf2,yf2,ex)
	else 
	  call Ellipse(a,b,c,d,e,f,typ,l,m,xc,yc,xv1,yv1,xv2,yv2,la,lb,xf1,yf1,xf2,yf2,ex)
    end if
  end if

  ! Este pedazo es para imprimir los resultados de manera adecuada.
100 SELECT CASE(typ)
    case (1)
        print *,'  Tipo: Elipse'
		print *,''
        write(*,300) xc, yc
        write(*,301) xv1, yv1
		write(*,302) xv2, yv2
		write(*,303) la
		write(*,304) lb
		write(*,305) xf1, yf1
		write(*,306) xf2, yf2
		write(*,307) ex
    case (2)
        if (a+c.eq.0) then
		  print *,'  Tipo: Hiperbola Equilatera'
        else 
		  print *,'  Type: Hiperbola'
        end if
		print *,''
        write(*,300) xc, yc
		write(*,310) xv1, yv1
        write(*,311) xv2, yv2
		write(*,312) xs1, ys1
        write(*,313) xs2, ys2
		write(*,305) xf1, yf1
		write(*,306) xf2, yf2
		write(*,307) ex
    case (3)
        print *,'  Tipo: Parabola'
		print *,''
		write(*,300) xc, yc
        write(*,314) xv1, yv1
		write(*,315) xf1, yf1
        write(*,316) ex
    case (4)
        print *,'  Tipo: Circulo'
		print *,''
        write(*,300) xc, yc
		write(*,320) la
        write(*,307) ex
    case (5) 
	    print *,'  Degenerada a linea.'
    case (6) 
	    print *,'  Degenerada a dos lineas.'
    case (7)
	    print *,'  Degenerada a un punto.'
    case (8) 
	    print *,'  No es conica !'

	END SELECT

  print *,''; print *,''
  stop

200 format('    a = ')
201 format('   2b = ')
202 format('    c = ')
203 format('   2d = ')
204 format('   2e = ')
205 format('    f = ')

300 format('   Centro                :  x=',F9.6,'  y=',F9.6)
301 format('   Eje mayor             :  x=',F5.2,'  y=',F5.2)!Eje mayor, se da un vector con la
302 format('   Eje menor             :  x=',F5.2,'  y=',F5.2)!dirección del eje mayor(y el menor)
303 format('   DistanciaM eje mayor  : ',F9.6)
304 format('   DistanciaM eje menor  : ',F9.6)    !DistanciaM significa Distancia Media
305 format('   Foco 1                :  x=',F9.6,'  y=',F9.6)
306 format('   Foco 2                :  x=',F9.6,'  y=',F9.6)
307 format('   Excentricidad          :  ',F10.8)

310 format('   Eje 1                 :  x=',F5.2,'  y=',F5.2)
311 format('   Eje 2                 :  x=',F5.2,'  y=',F5.2)
312 format('   Cresta 1              :  x=',F9.6,'  y=',F9.6)
313 format('   Cresta 2              :  x=',F9.6,'  y=',F9.6)
314 format('   Eje de Simetría       :  x=',F5.2,'  y=',F5.2)!lo mismo que arriba, en la sección de ejes
315 format('   Foco                  :  x=',F9.6,'  y=',F9.6)!se da un vector que apunta en la dirección 
316 format('   Parámetro             :  ',F10.8)             !de los mismos

320 format('   Radio                 : ',F9.6)

END
! aqui termina el programa principal, abajo estasn las subrrutinas correspondiantes a cada conica.

Subroutine Parabola(a,b,c,d,e,f,typ,l,m,xc,yc,xv1,yv1,xf1,yf1,ex)
    integer typ
    real*8 a,b,c,d,e,f,l,m,xc,yc,xv1,yv1,xf1,yf1,ex
    real*8 x,y
    typ=3
    if (c.eq.0 .and. a.eq.0) then !Caso en que la parabola no existe o esta degenerada en una linea
      if (d.eq.0 .and. e.eq.0) then
	    typ=8
	  else 
	    typ=5   !8=no es conica, 5=es una linea
        goto 100
      end if
    end if
    if (a.eq.0) then
      x2=1; y2=0; l=0; m=1
    else
      if (a<0) then
        f=-f; e=-e; d=-d
        c=-c; b=-b; a=-a
      end if
      l=dsqrt(a); m=dsqrt(c)
      if (b<0) m=-m
      u=dsqrt(a+c)
      x2=m/u; y2=-1.d0/u
      f=f*u;  c=(a+c)*u
      u=d*m-e*l; e=d*l+e*m; d=u
    end if
    if (d.eq.0) then
      if (e*e<c*f) then
	    typ=8
	  else 
	    typ=6   !8=no es conica, 6=Degenerada a dos lineas
        goto 100
      end if
    else
      x=(e*e-c*f)/2.d0/c/d; y=-e/c
      xc=x*x2-y*y2; yc=y*x2+x*y2
      ex=-d/c
      xf1=xc+ex*x2/2.d0; yf1=yc+ex*y2/2.d0
      xv1=m; yv1=-l
    end if
100 return
end  
                 
  
Subroutine Hyperbola(a,b,c,d,e,f,typ,l,m,xc,yc,xv1,yv1,xv2,yv2,xs1,ys1,xs2,ys2, &
                       xf1,yf1,xf2,yf2,ex)
    integer typ
	real*8 a,b,c,d,e,f,l,m,xc,yc,xv1,yv1,xv2,yv2,xs1,ys1,xs2,ys2,xf1,yf1,xf2,yf2,ex
	real*8 u,la,lb
    typ=2
    la=dsqrt(-dabs(f)/l) 
	lb=dsqrt(dabs(f)/m)
    if (f<0) then
      u=la; la=lb; lb=u
      u=x2; x2=-y2; y2=u
      u=xv1; xv1=-yv1; yv1=u
    end if
    xv2=-yv1; yv2=xv1
    u=dsqrt(la*la+lb*lb)
    xs1=xc+x2*la; ys1=yc+y2*la
    xs2=xc-x2*la; ys2=yc-y2*la
    xf1=xc+x2*u; yf1=yc+y2*u
    xf2=xc-x2*u; yf2=yc-y2*u
    ex=u/la
	return
  end

  Subroutine Ellipse(a,b,c,d,e,f,typ,l,m,xc,yc,xv1,yv1,xv2,yv2,la,lb,xf1,yf1,xf2,yf2,ex)
    integer typ
	real*8 a,b,c,d,e,f,l,m,xc,yc,xv1,yv1,xv2,yv2,la,lb,xf1,yf1,xf2,yf2,ex
	real*8 u
    typ=1
    if (f*l>0) then
	  typ=8
	  return  !8=no es conica
    end if
    la=dsqrt(-f/l); lb=dsqrt(-f/m)
    if (l<0) then
      u=la; la=lb; lb=u
      u=x2; x2=-y2; y2=u
      u=xv1; xv1=-yv1; yv1=u
    end if
    xv2=-yv1; yv2=xv1
    u=dsqrt(la*la-lb*lb)
    xf1=xc+x2*u; yf1=yc+y2*u
    xf2=xc-x2*u; yf2=yc-y2*u
    ex=u/la
	return
  end




