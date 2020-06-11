import random
import numpy as np
import matplotlib.font_manager as font_manager

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=12)

def MCint_area(f, a, b, n, m):
    below = 0  # counter for no of points below the curve
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            below += 1
    area = below/float(n)*m*(b-a)
    return area


def MCint_area_vec(f, a, b, n, m):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, m, n)
    below = np.sum(y < f(x))
    area = below/float(n)*m*(b-a)
    return area

def MCint3_area(f, a, b, n, m, N=1000):
    # Store every N intermediate integral approximations in an
    # array I and record the corresponding k value.
    I_values = []
    k_values = []
    below = 0  # counter for no of points below the curve
    for k in range(1, n+1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            below += 1
        area = below/float(k)*m*(b-a)
        if k % N == 0:
            I = area
            I_values.append(I)
            k_values.append(2*k)
    return k_values, I_values


def f1(x):
    return 2 + 3*x

a = 1; b = 2; n = 1000000; N = 10000; fmax = f1(b)

t0 = time.clock()
print (MCint_area(f1, a, b, n, fmax))
t1 = time.clock()
print (MCint_area_vec(f1, a, b, n, fmax))
t2 = time.clock()
print ('fraccion bucle/vectorizada:', (t1-t0)/(t2-t1))

k, I = MCint3_area(f1, a, b, n, fmax, N)
print (I[-1])

error = 6.5 - np.array(I)

plt.plot(k, error)
plt.xlabel('Número de muestras', fontproperties=font_prop)
plt.ylabel('Error', fontproperties=font_prop)
plt.title('Integración Monte Carlo por puntos', fontproperties=font_prop)
plt.savefig('integracionPuntos.eps')
plt.show()
