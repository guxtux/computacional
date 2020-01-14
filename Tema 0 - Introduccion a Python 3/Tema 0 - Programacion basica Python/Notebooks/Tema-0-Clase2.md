# Estructuras de control.

En cualquier lenguaje de programación se incluye una serie de estructuras de control para ampliar las posibilidades de ejecución de un programa.

##
En python manejaremos las estructuras más comunes que son relativamente sencillas de usar, cuidado siempre de manejar la sintaxis respectiva.

# <font color="Cyan">1. Condicionales</font>

Una sentencia condicional permite evaluar si se cumple cierta condición, es decir, si su valor es True, se ejecuta el bloque que puede contener una o más instrucciones, en caso de que el valor de la condición no se cumpla, es decir, el valor sea False, no se ejecuta la(s) instrucción(es) contenida(s) y se sigue a la siguiente línea de código.

##
El bloque condicional más simple utiliza la instrucción **if**, a continuación lleva una expresión que debe de evaluarse, como se mencionó antes, el valor de la expresión debe de ser True para que se ejecute(n) la(s) instrucción(es) contenidas en el bloque.

##
Hay dos puntos (:) que identifican el bloque y las instrucciones contenidas deben de estar identadas, en caso contrario, python nos devolverá un mensaje de error provocado por la identación equivocada.

## La evaluación de la expresión es verdadera. 

```python
a = 10
if a > 0:
    print ('la variable a es positiva')
    a = a + 1

print (a)
```

---

    la variable a es positiva
    11

##
En el ejemplo asignamos a la variable <font color="yellow">a</font> el valor de <font color="yellow">10</font>, en el bloque condicional se evalúa la expresión <font color="yellow">a > 0</font>

##
En el ejemplo, el valor que se obtiene es True, por tanto, se ejecutan las instrucciones que están contenidas dentro del bloque, que son:

1. Mostrar en pantalla la línea *la variable a es positiva*
2. Se incrementa una unidad el valor de <font color="yellow">a</font>

##
Aquí concluyen las instrucciones dentro del condicional, la siguiente función *print* está fuera del bloque, y nos muestra el valor de la variable <font color="yellow">a</font>, que en el ejemplo ahora es *11*.

## La evaluación de la expresión es falsa. 

```python
a = 0
if a > 0:
    print ('la variable a es positiva')
    a = a + 1

print (a)
```

---

    0

##
Ahora vemos que el valor de la variable <font color="yellow">a</font> es cero, y al evaluarse la expresión <font color="yellow">a > 0</font>, el resultado es False

##
Por tanto **NO** se ejecuta instrucción alguna que está dentro del bloque, y continua el código hacia la siguiente línea, en el ejemplo continua con la función *print*.

## Alternativas para la evaluación de un condicional. 

##
**Alternativa 1 para el bloque condicional.**

En ocasiones necesitaremos hacer que el programa realice alguna instrucción cuando la expresión que se evalúa en el <font color="yellow">if</font> sea falsa, es decir, que haya una respuesta en particular para el caso en que obtengamos un valor False en la evaluación de la expresión.

##
Para ello, podemos ocupar la instrucción <font color="yellow">else:</font> que se escribe en el mismo nivel de identación que la instrucción <font color="yellow">if</font> y lleva también dos puntos <font color="yellow">(:)</font>

##
Las instrucciones que están contenidas dento de <font color="yellow">else:</font> se ejecutarán siempre y cuando la expresión que se evalúa, sea falsa.

En python no se pide otra expresión para evaluar, sino que se ejecutan inmediatamente cuando se evalúa que el resultado de la expresión es False.

##
```python
a = -2
if a > 0:
    print ('la variable a es positiva')
    a = a + 1
else:
    print ('la variable a es negativa')
```

---

    la variable a es negativa

##
En el ejemplo vemos que el valor de <font color="yellow">a</font> es $-2$.

La expresión que se evalúa en el <font color="yellow">if</font> es False, por tanto, no se ejecutan las instrucciones contenidas dentro del <font color="yellow">if</font>, sino que se va a ejecutar la(s) instrucción(es) contenida(s) en el <font color="yellow">else:</font>

##
Si la expresión inicial que se evalúa es True, se ejecutan las instrucciones contenidas en el bloque <font color="yellow">if</font>, y ya no se ejecuta instrucción alguna del bloque <font color="yellow">else:</font>, para posteriormente continuar con el programa.

##
**Alternativa 2 para el bloque condicional**.

El uso de un bloque <font color="yellow">if ... else</font> nos da oportunidad manejar el código en caso de obtener un valor False en la evaluación de la expresión.

##
Como ya mencionamos, no se requiere evaluar otra expresión, pero podemos usar una variante del condicional y evaluar una nueva expresión (que sería diferente de la primera) y con ello, nuestro algoritmo gana bastante potencial para responder a nuestras necesidades, y eso lo haremos con el bloque <font color="yellow">if ... elif ... else</font>

##
```python
a = 0
if a > 0:
    print ('la variable a es positiva')
    a = a + 1
elif a == 0:
    print ('la variable a es cero')
else:
    print ('la variable a es negativa')
```

---

    la variable a es cero

##
La primera expresión <font color="yellow">a > 0</font> tiene un valor False, por tanto, continua el código hasta la sentencia <font color="yellow">elif:</font>

En ésta se evalúa la nueva expresión <font color="yellow">a == 0</font>, que resulta ser True.

##
Por tanto se ejecuta la instrucción contenida en el bloque <font color="yellow">elif:</font>, saliendo luego del bloque y continua el código, es decir, ya no se revisa el <font color="yellow">else:</font>

##
```python
a = eval(input('Introduce el valor de a'))
if a > 0:
    print ("a es positivo")
    a = a + 1
elif a == 0:
    print ("a es 0")
else:
    print ("a es negativo")
```

---

    Introduce el valor de a0
    a es 0


# <font color="Cyan">2. Bucles</font>

Un bucle es una sentencia que evalúa inicialmente una condición, en caso de que se cumple (valor True) se ejecuta(n) un conjunto de instrucciones, posteriormente, se revisa el valor de la condición, mientras sea verdadero, las instrucciones se ejecutan nuevamente.

##
**Tipos de bucles**

Hay que considerar dos posibles casos en el manejo de los bucles:

1. Cuando conocemos el número de ciclos que van a realizarse.
2. Cuando no sabemos cuántas veces se requiere que el ciclo se repita.

##
En ambos casos se necesita modificar alguna variable y evaluar nuevamente una condición, de tal manera que se cumpla con cierto criterio y concluya el bucle.

##
En caso contrario, tendremos lo que se denomina un *bucle infinito*, es decir, el conjunto de instrucciones se va a repetir indefinidamente, por lo que hay que ''cortar'' el programa en ejecución.

## El bucle # <font color="yellow">while</font>

El ciclo/bucle <font color="yellow">while</font> tiene la siguiente sintaxis:

```python
while condicion:
    instruccion1
    instruccion2
    ....
```

##
Las instrucciones contenidas en el bloque se van a ejecutar mientras el valor de la condición sea verdadero.

Para salir del ciclo, el valor de la condición debe devolver False, por lo que es necesario que dentro de este bloque, se realice alguna modificación a la(s) variable(s) contenida(s) en la condición.

##
```python
nMax = 5
n = 1
a = [] 
while n < nMax:
    a.append(1.0/n) 
    n = n + 1
print (a)
```

---

    [1.0, 0.5, 0.3333333333333333, 0.25]

##
En el ejemplo definimos la variable <font color="yellow">nMax = 5</font>, se toma un valor inicial para la variable <font color="yellow">n</font>, y se crea una lista vacía <font color="yellow">a</font>.

##
Como la expresión que se evalúa luego del <font color="yellow">while</font> es True ya que <font color="yellow">n < nMax</font>

Se ejecuta lo que está contenido dentro del ciclo: se agrega un nuevo elemento a la lista, mediante la instrucción <font color="yellow">a.append</font>, y luego se incrementa el valor de <font color="yellow">n</font> en una unidad.

##
Llega el momento en que se evalúa la expresión <font color="yellow">5 < 5</font> que devuelve un valor False por tanto, termina el ciclo.

##
```python
from random import random
x = 0.2
a = 0
while x < 0.8:
    # a = a + 1
    a += 1
    x = random()
    print (x)
print ("\n Acabo el bucle luego de ", a, " iteraciones")
```

---

    0.0440045786139075
    0.7796230779526429
    0.8946464576298329
    
     Acabo el bucle luego de  3  iteraciones


## El ciclo/bucle <font color="yellow">for</font>. 

La sintaxis del bucle/ciclo $\texttt{for}$ es la siguiente:

```python
for variable in lista:
    instruccion1
    instruccion2
    ...
```

##
El conjunto de instrucciones contenidas dentro del bucle se va a ejecutar mientras no se acabe de recorrer la lista; el valor de la variable, será el elemento de la lista que está siendo tratado en ese momento:

##
```python
cubos =[]
for i in range(7):
    ic = i**3
    cubos.append(ic)
    print (i, cubos)
```

---

    0 [0]
    1 [0, 1]
    2 [0, 1, 8]
    3 [0, 1, 8, 27]
    4 [0, 1, 8, 27, 64]
    5 [0, 1, 8, 27, 64, 125]
    6 [0, 1, 8, 27, 64, 125, 216]

##
**Algunas cosas más sobre el ciclo <font color="yellow">for</font>**

La instrucción <font color="yellow">for</font> no sólo itera sobre enteros: el ciclo <font color="yellow">for</font>$ itera sobre todos los elementos de una *secuencia*, asignando el valor del elemento a la variable.

En el ejemplo anterior, la función <font color="yellow">range</font> es sólo una función conveniente que genera una lista de enteros.

##
```python
for i in [ 3, 1, 4, 1, 5, 9, 2, 6, 5, 3 ]:
    print ("Un digito de pi es", i)
```

---

    Un digito de pi es 3
    Un digito de pi es 1
    Un digito de pi es 4
    Un digito de pi es 1
    Un digito de pi es 5
    Un digito de pi es 9
    Un digito de pi es 2
    Un digito de pi es 6
    Un digito de pi es 5
    Un digito de pi es 3

##
```python
for i in [ 1, 2, 3, 4 ] + [ 3, 2, 1 ]:
    print (i)
```

---

    1
    2
    3
    4
    3
    2
    1

###
```python
for i in " estas son palabras al azar ".split ():
    print (i)
```

---

    estas
    son
    palabras
    al
    azar


## Ejemplos del ciclo <font color="yellow">for</font>

```python
for i in range(10):
    print (i)
```

---

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

##
```python
for i in range(1,10):
    print (i)
```

---

    1
    2
    3
    4
    5
    6
    7
    8
    9

##
```python
for j in range(10,1,-1):
    print (j)
```

---

    10
    9
    8
    7
    6
    5
    4
    3
    2

##
```python
lista = ['adios', 'mundo', 'cruel']
for palabra in lista:
    print (palabra)
```

---

    adios
    mundo
    cruel


## Ciclo <font color="yellow">for</font> más elaborado. 

El siguiente código usa los elementos de lista y busca la coincidencia exacta del nombre que proporciona el usuario en la línea de comandos, en caso de que no lo encuentre, le avisa al usuario que ese nombre no está en la lista inicial.

##
```python
lista = ['Hugo', 'Paco', 'Luis', 'McPato']
nombre = input('Teclea un nombre: ')

for i in range(len(lista)):
    if lista[i] == nombre:
        print (nombre, ' es el numero ', i + 1, ' en la lista')
        break
else:
        print (nombre, ' no esta en la lista')
```

---

    Teclea un nombre: Hugo
    Hugo  es el numero  1  en la lista

##
En el ejemplo anterior, vemos que hay una sentencia <font color="yellow">else:</font> al mismo nivel de alineación del ciclo <font color="yellow">for</font>, efectivamente, esta sentencia <font color="yellow">else:</font> no pertenece al condicional <font color="yellow">if</font>, sino al bloque <font color="yellow">for</font>.

##
La sentencia <font color="yellow">else:</font> la podemos utilizar tanto para los bucles <font color="yellow">for</font> y <font color="yellow">while</font>.

## **Instrucciones <font color="yellow">break</font> y <font color="yellow">continue</font>**.

Hay dos instrucciones que permiten ''salirse'' de un bucle sin necesidad de esperar a que en un ciclo <font color="yellow">while</font> la expresión que se evalúa cambie a un valor False, y para un ciclo <font color="yellow">for</font>, esperar a que se recorran todos los elementos de la lista.

##
La instrucción es <font color="yellow">break</font>, veamos en el siguiente ejemplo, cómo se usa.

##
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print (n, ' es igual a ', x, '*', n/x)
            break
    else:
        print (n, ' es numero primo')
```

---

    2  es numero primo
    3  es numero primo
    4  es igual a  2 * 2.0
    5  es numero primo
    6  es igual a  2 * 3.0
    7  es numero primo
    8  es igual a  2 * 4.0
    9  es igual a  3 * 3.0

##
Tenemos dos ciclos <font color="yellow">for</font> anidados (hay que tener siempre cuidado con la identación) 

En el segundo ciclo, tenemos un condicional <font color="yellow">if</font> contenido, se evalúa con la función módulo, para expresar que un número es producto de otro

##
Tenemos la instrucción <font color="yellow">break</font>, que no se espera a que se complete el recorrido de los elementos de la lista con índice <font color="yellow">x</font>, que va desde <font color="yellow">2</font> hasta <font color="yellow">n</font>

##
Continua con un incremento en el contador <font color="yellow">n</font> del primer ciclo <font color="yellow">for</font>.

En caso de que no haya un residuo igual a cero, entonces el número es primo, aquí nos apoyamos en la sentencia <font color="yellow">else</font> del ciclo <font color="yellow">for</font>.

## *Uso de la instrucción <font color="yellow">continue</font>*

La instrucción <font color="yellow">continue</font>, lo que hace, es dar paso a la siguiente iteración del ciclo, veamos el ejemplo:

##
```python
for num in range(2,10):
    if num % 2 == 0:
        print ('Encontre un numero par ', num)
        continue
    print ('Encontre un numero ', num)
```

---

    Encontre un numero par  2
    Encontre un numero  3
    Encontre un numero par  4
    Encontre un numero  5
    Encontre un numero par  6
    Encontre un numero  7
    Encontre un numero par  8
    Encontre un numero  9

# Ejercicio completo.

## Carrera de bicicletas: el efecto de la resistencia al aire.

##
La bicicleta es una forma muy eficiente de transporte, esto la sabe quien se ha subido a una.

El objetivo con este ejercicio es entender los factores que determinan la velocidad máxima de una bicicleta y estimar esta velocidad para un caso realista. 

##
Comenzaremos ignorando la fricción; se tiene que considerar posteriormente, pero primero vamos a entender cómo lidiar con el caso más simple sin fricción.

##
Partimos con la ecuación de movimiento:segunda ley de Newton, que puede escribirse en la forma

Donde v es la velocidad, m es la masa de la combinación bicicleta-ciclista, t es el tiempo y F es la fuerza sobre la bicicleta que viene del esfuerzo del ciclista (aquí asumiremos que la bicicleta se está moviendo en plano terreno).

##
Manejar debidamente con F es complicado por la mecánica misma de una bicicleta: ya que la fuerza ejercida por el ciclista se transmite a las ruedas por medio del plato, engranajes, etc.

##
Esto hace muy difícil obtener una expresión exacta para F.

Sin embargo, hay otra manera de atacar este problema que evita la necesidad de conocer la fuerza.

##
Este enfoque alternativo implica formular el problema en términos de la potencia generada por el conductor. 

Los estudios fisiológicos de ciclistas de élite de carreras han demostrado que estos atletas son capaces de producir una potencia de salida de aproximadamente 400 watts durante largos períodos de tiempo (1 h)

##
Usando ideas de trabajo-energía podemos reescribir la ecuación anterior como

##
Donde E es la energía total de la combinación bicicleta-ciclista, y P es la potencia de salida del ciclista.

(Esto supone implícitamente que se pierde muy poca energía para la fricción en la propia bicicleta, incluiremos otras fuentes de fricción en un momento).

##
Para un recorrido plano toda la energía es cinética, entonces $E = mv^{2}$ y $dE/dt = mv (dv/dt)$.

##
Al sustituir en la ecuación anterior

##
Si P es constante, se puede resolver analíticamente. Ordenando los términos

$\<int_v_>0</int_v_>v