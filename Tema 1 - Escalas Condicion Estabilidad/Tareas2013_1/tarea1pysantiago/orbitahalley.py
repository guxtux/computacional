#y = [u,u']
def kepler(y,t,A):
        #A = G*M*m**2/L**2 = G*M/r**4/(dTheta/dT)**2
        return sp.array([y[1],-y[0]+A])
	t = sp.linspace(0,2*sp.pi,1000)
	y = integrate.odeint(kepler,sp.array([1,0.2]),t,(2,))
	x = sp.cos(t)/u[:,0]
	y = sp.sin(t)/u[:,0]
	pylab.plot(x,y)
	# Marco el origen
	pylab.scatter([0],[0],marker='x')
	pylab.show()
