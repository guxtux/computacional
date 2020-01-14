
# Operadores aritméticos
## Python como calculadora

Una vez abierta la sesión en $\texttt{python}$, podemos aprovechar al máximo este lenguaje: contamos con una calculadora a la mano, sólo hay que ir escribiendo las operaciones en la línea de comandos.

## Podemos hacer una suma:

```python
3+200
```

---

    203


## Una división entre enteros

```python
30/1234
```

---

    0.024311183144246355


## Una división entre reales
```python
3.0/4.0
```

---

    0.75



## Una división entera
### Devuelve el cociente (sin decimales)
```python
30//4
```

---

    7


## Otro ejemplo

```python
4//3
```

---

    1


## La división devuelve un determinado número de dígitos luego del punto decimal

```python
4/3
```

---

    1.3333333333333333



## Combinación de operadores
```python
5.0 / 10 * 2 + 5
```

---

    6.0

**¿por qué obtenemos este resultado??**

## El resultado cambia cuando agrupamos con paréntesis

```python
5.0 / (10 * 2 + 5)
```

---

    0.2

Como podemos ver, el uso de paréntesis en las expresiones tiene una particular importancia sobre la manera en que se evalúan las expresiones

## Potenciación de un número

Podemos elevar un número a una potencia en particular

```python
2**3**2
```

---

    512

## Orden para las potencias

Vemos que elevar a una potencia, la manera en que se ejecuta la expresión se realiza en un sentido en particular: de derecha a izquierda


```python
(2**3)**2
```

---

    64

## Los paréntesis

El uso de paréntesis nos indica que la expresión contenida dentro de ellos, es la que se evalúa primero, posteriormente se sigue la regla de precedencia de operadores

## Operador módulo

El operador módulo $(\%)$ nos devuelve el residuo del cociente


```python
17%3
```

---

    2

# Tabla de operadores
## Precedencia en los operadores aritméticos

##
|Operador|Operación|Ejemplo|Resultado|
|:------:|---------|-------|---------|
| $**$    | Potencia     |$2**3$ | $8$     |
| $*$     |Multiplicación  |$7*3$    |$21$   |
| $/$       |División        |$10.5/2$ |$5.25$ |
| $//$      |Div. entera |$10.5//2$|$5.0$  |
| $+$       |Suma            |$3+4$    |$7$    |
| $-$       |Resta           |$6-8$    |$-2$   |
| $\%$      |Módulo          |$15\%6$  |$3$    |

## Precedencia de los operadores artiméticos 1

1. Las expresiones contenidas dentro de pares de paréntesis son evaluadas primero. En el caso de expresiones con paréntesis anidados, los operadores en el par de paréntesis más interno son aplicados primero.

## Precedencia de los operadores artiméticos 2
2. Las operaciones de exponentes son aplicadas después. Si una expresión contiene muchas operaciones de exponentes, los operadores son aplicados de derecha a izquierda.

## Precedencia de los operadores artiméticos 3
3. La multiplicación, división y módulo son las siguientes en ser aplicadas. Si una expresión contiene muchas multiplicaciones, divisiones u operaciones de módulo, los operadores se aplican de izquierda a derecha.

## Precedencia de los operadores artiméticos 4
4. Suma y resta son las operaciones que se aplican por último. Si una expresión contiene muchas operaciones de suma y resta, los operadores son aplicados de izquierda a derecha. La suma y resta tienen el mismo nivel de precedencia.


# Operadores relacionales

##
Se comparan dos (o más expresiones) mediante un operador, el tipo de dato que devuelve es lógico: $\textbf{True}$ o $\textbf{False}$, que también tienen una representación de tipo numérico:

* $\textbf{True}$ = 1
* $\textbf{False}$ = 0

## Operaciones aritméticas y relacionales

```python
1 + 2 > 7- 3
```

---

    False

## Se pueden combinar diferentes expresiones

```python
1 < 2 < 3
```

---

    True

## El doble signo igual (==) es el operador de igualdad


```python
1 > 2 == 2 < 3
```

```python
1 > (2 ==  2) <3
```

---

    False


## Combinación de expresiones

```python
3 > 4 < 5
```

---

    False

## 
Hay que tener cuidado con el uso de operadores relaciones estrictos

```python
1.0 / 3 < 0.3333
```

---

    False

##
Las expresiones se pueden complicar cada vez más, por lo que hay que mantener atención al momento de escribirlas

```python
5.0 / 3 >= 11 /7.0
```

---

    True

##
El utilizar las operaciones aritméticas y relacionales, extiende por mucho el uso del lenguaje.

```python
2**(2. /3) < 3**(3./4)
```

---

    True

## Tabla de operadores relacionales

|Operador|Operación|Ejemplo|Resultado|
|:-------:|------------|-------|---------|
|$==$     |Igual a        | $4==5$      |$\texttt{False}$|
|$!=$     |Diferente      | $2!=3$      |$\texttt{True}$ |
|$<$      |Menor que      | $10<4$      |$\texttt{False}$|
|$>$      |Mayor que      | $5>-4$      |$\texttt{True}$ |
|$<=$     |Menor o igual  | $7<=7$      |$\texttt{True}$ |
|$>=$     |Mayor o igual  | $3.5 >= 10$ |$\texttt{False}$|


#  Operadores booleanos
## Operadores booleanos
En el caso del operador boleano <font color="yellow"><b>and</b></font> y el operador <font color="yellow"><b>or</b></font> evalúan una expresión compuesta por dos (o más términos).

##
En ambas expresiones se espera que cada una tenga el valor de <font color='green'>True</font>, en caso de que esto ocurra, el valor que devuelve la evaluación, es <font color='green'>$\texttt{True}$</font>.

##
Como se verá en la tabla de verdad, se necesita una condición particular para que el valor que devuelva la comparación, sea <font color='red'>$\texttt{False}$</font>.

|Operador|Operación|Ejemplo|Resultado|
|--------|---------|-------|---------|
|$\texttt{and}$ |Conjunción |$\texttt{False and True}$  |$\texttt{False}$|
|$\texttt{or}$  |Disyunción |$\texttt{False or True}$   |$\texttt{True}$|
|$\texttt{not}$ |Negación   |$\texttt{not True}$        |$\texttt{False}$|

## Tabla de verdad de los operadores boleanos

##

| A       | B       | A and B | A or B  | not A   |
|:-------:|:-------:|:-------:|:-------:|:-------:|
| True    | True    | True    | True    | <font color=red>False</font>   |
| True    | <font color=red>False</font>   | <font color=red>False</font>   | True    | <font color=red>False</font>   |
| <font color=red>False</font>   | True    | <font color=red>False</font>   | True    | True    |
| <font color=red>False</font>   | <font color=red>False</font>   | <font color=red>False</font>   | <font color=red>False</font>   | True    |

# Tipos de variables

##
Las variables en python sólo son ubicaciones de memoria reservadas para almacenar valores.

Esto significa que cuando se crea una variable, se reserva un poco de espacio disponible en la memoria.

##
Basándose en el tipo de datos de una variable, el intérprete asigna memoria y decide qué se puede almacenar en la memoria reservada.

Por lo tanto, al asignar diferentes tipos de datos a las variables, se pueden almacenar **enteros**, **decimales** o **caracteres (cadenas)** en estas variables.



## Asignando valores a variables

Las variables de python no necesitan una declaración explícita para reservar espacio de memoria. 

La declaración ocurre automáticamente cuando se asigna un valor a una variable. *El signo igual (=) se utiliza para asignar valores a las variables*.

##
El término a la izquierda del operador = es el *nombre de la variable* y el término a la derecha del operador = es el *valor almacenado* en la variable.

## Ejemplos

```python
contador = 100          # Asignacion de tipo entero
distancia = 1000.0      # De punto flotante
nombre = "Chucho"       # Una cadena de caracteres

print (contador)
print (distancia)
print (nombre)
```

---

    100
    1000.0
    Chucho


## Asignación múltiple de valores

En python podemos asignar un valor único a varias variables simultáneamente.

##

```python
A = b = c = 1
print (A)
print (b)
print (c)
```

---

    1
    1
    1

##
En el ejemplo, se crea un objeto entero con el valor $1$, y las tres variables se asignan a la misma ubicación de memoria. 

##
También puede asignar varios objetos a varias variables.

```python
A, b, c = 1, 2, "Alicia"
print (A)
print (b)
print (c)
```

---

    1
    2
    Ana

##
Aquí, dos objetos enteros con valores $1$ y $2$ se asignan a las variables $A$ y $b$ respectivamente, y un objeto de cadena con el valor **Alicia** se asigna a la variable $c$.

# Tipos de Datos Estándar

Los datos almacenados en la memoria pueden ser de varios tipos. Por ejemplo, la edad de una persona se almacena como un valor numérico y su dirección se almacena como caracteres alfanuméricos.

##
En python se cuenta con varios tipos de datos estándar que se utilizan para definir las operaciones posibles entre ellos y el método de almacenamiento para cada uno de ellos.

##
Los tipos de datos son cinco:

1. <font color="yellow"> Números</font>.
2. <font color="yellow"> Cadena</font>.
3. <font color="yellow"> Lista</font>.
4. <font color="yellow"> Tupla</font>.
5. <font color="yellow"> Diccionario</font>.

## <font color="yellow">Números</font> 

Los tipos de datos numéricos almacenan valores numéricos.

Los objetos numéricos se crean cuando se les asigna un valor.

##
```python
Var1 = Var2 = 10
print (Var1)
print (Var2)
```

---

    10
    10

##
También se puede eliminar la referencia a un objeto numérico utilizando la sentencia <font color= "Chartreuse ">del</font>

La sintaxis de la sentencia <font color= "Chartreuse ">del</font> es:

$del$  $var1 [, var2 [, var3 [...., varN]]]]$

##
Se puede eliminar un solo objeto o varios objetos utilizando la sentencia <font color= "Chartreuse ">del</font>

Por ejemplo:
```python
del var

del variable1, variable2
```

##
En python se soportan tres tipos numéricos diferentes:

1. <font color="Cyan">Int (enteros con signo)</font>
2. <font color="DarkOrange">Flotante (valores reales de punto flotante)</font>
3. <font color="Snow">Complejos (números complejos)</font>

##
Un número complejo consiste en un par ordenado de números reales de coma flotante denotados por

$$x + yj$$

donde $x$ e $y$ son números reales, $yj$ es la unidad imaginaria.

##
Todos los números enteros en python 3 se representan como enteros largos.

##
|$\texttt{int}$      |$\texttt{float}$    |$\texttt{complex}$   |
|:------------------:|:------------------:|:------------------: |
|$\texttt{10}$       | $\texttt{0.0}$     | $\texttt{3.14j}$    |
|$\texttt{100}$      | $\texttt{15.20}$   | $\texttt{45.j}$     |
|$\texttt{100}$      | $\texttt{15.20}$   | $\texttt{45.j}$     |
|$\texttt{080}$      | $\texttt{32.3+e18}$| $\texttt{0.876j}$   |
|$\texttt{-0490}$    | $\texttt{-90.}$    | $\texttt{-.645+0j}$ |
|$\texttt{-0x260}$   | $\texttt{-32.54e100}$ |$\texttt{3e+26j}$ |
|$\texttt{0x69}$     | $\texttt{70.2-E12}$ | $\texttt{4.53e-7j}$|

## <font color="yellow">Cadenas</font> 

Las cadenas en $\texttt{python}$ se identifican como un conjunto contiguo de caracteres representados en las comillas. 

Con python se permite cualquier par de comillas simples o dobles.

##
Los subconjuntos de cadenas pueden ser tomados usando el operador de corte ($[\;]$ y $[:]$) con índices comenzando en $0$ al inicio de la cadena hasta llegar a $-1$ al final de la misma.

##
El signo más ($+$) es el operador de concatenación de cadenas y el asterisco ($*$) es el operador de repetición.

##

```python
cadena = 'Hola Mundo!'

print (cadena)          # Presenta la cadena completa
print (cadena[0])       # Presenta el primer caracter de la cadena
print (cadena[2:5])     # Presenta los caracteres de la 3a a la 5a posicion
print (cadena[2:])      # Presenta la cadena que inicia a partir del 3er caracter
print (cadena * 2)      # Presenta dos veces la cadena
print (cadena + "PUMAS") # Presenta la cadena y concatena la segunda cadena
```

---

    Hola Mundo!
    H
    la 
    la Mundo!
    Hola Mundo!Hola Mundo!
    Hola Mundo!PUMAS


## <font color="yellow">Listas</font>

Las listas es el tipo de dato más versátil de los tipos de datos compuestos de python.

Una lista contiene elementos separados por comas y entre corchetes ($[ \; ]$).

##
En cierta medida, las listas son similares a los arreglos (arrays) en el lenguaje C.

Una de las diferencias entre ellos es que todos los elementos pertenecientes a una lista pueden ser de tipo de datos diferente.

##
Los valores almacenados en una lista se pueden acceder utilizando el operador de división ($[ \; ]$ y $[:]$) con índices que empiezan en $0$ al principio de la lista y opera hasta el final con $-1$.

##
El signo más ($+$) es el operador de concatenación de lista y el asterisco ($*$) es el operador de repetición.

##
```python
milista = [ 'abcd', 786 , 2.23, 'salmon', 70.2 ]
listabreve = [123, 'pizza']

print (milista)              # Presenta la lista completa
print (milista[0])          # Presenta el primer elemento de la lista
print (milista[1:3])        # Presenta los elementos a partir de la 2a posiciona hasta la 3a
print (milista[2:])          # Presenta los elementos a partir del 3er elemento
print (listabreve * 2)       # Presenta dos veces la lista
print (milista + listabreve) # Presenta la lista concatenada con la segunda lista
```

---

    ['abcd', 786, 2.23, 'salmon', 70.2]
    abcd
    [786, 2.23]
    [2.23, 'salmon', 70.2]
    [123, 'pizza', 123, 'pizza']
    ['abcd', 786, 2.23, 'salmon', 70.2, 123, 'pizza']

##  <font color="yellow">Tuplas</font>
Una tupla es otro tipo de datos de secuencia que es similar a la lista.

##
Una tupla consiste en un número de valores separados por comas. Sin embargo, a diferencia de las listas, las tuplas se incluyen entre <font color="Cyan">paréntesis</font>.

##
La principal diferencia entre las listas y las tuplas son:

1. Las listas están entre corchetes $[\;]$ y sus elementos y tamaño pueden cambiarse.
2. Las tuplas están entre paréntesis $(\;)$ y <font colo="Cyan">*no se pueden actualizar*</font>.

Las tuplas pueden ser consideradas como listas de sólo lectura.

##
```python
mitupla = ( 'abcd', 786 , 2.23, 'arena', 70.2  )
tuplabreve = (123, 'playa')

print (mitupla)                # Presenta la tupla completa
print (mitupla[0])             # Presenta el primer elemento de la tupla
print (mitupla[1:3])           # Presenta los elementos a partir del 2o elemento hasta la 3o
print (mitupla[2:])            # Presenta los elementos a partir del 3er elemento
print (tuplabreve * 2)         # Presenta dos veces la tupla
print (mitupla + tuplabreve)   # Preseta la tupla concatenada con la otra tupla
```

---

    ('abcd', 786, 2.23, 'arena', 70.2)
    abcd
    (786, 2.23)
    (2.23, 'arena', 70.2)
    (123, 'playa', 123, 'playa')
    ('abcd', 786, 2.23, 'arena', 70.2, 123, 'playa')

##
El siguiente código es inválido con la tupla, porque intentamos actualizar una tupla, que la acción no está permitida. El caso es similar con las listas.

##
```python
mitupla = ( 'abcd', 786 , 2.23, 'edificio', 70.2  )
milista = [ 'abcd', 786 , 2.23, 'energia', 70.2  ]
mitupla[2] = 1000    # Sintaxis invalida para la tupla
milista[2] = 1000     # Sintaxis invalida para la lista
```

---

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-a99f473d7b8f> in <module>()
          1 mitupla = ( 'abcd', 786 , 2.23, 'edificio', 70.2  )
          2 milista = [ 'abcd', 786 , 2.23, 'energia', 70.2  ]
    ----> 3 mitupla[2] = 1000    # Sintaxis invalida para la tupla
          4 milista[2] = 1000     # Sintaxis invalida para la lista


    TypeError: 'tuple' object does not support item assignment

##
Pero en la lista podemos agregar nuevos elementos que se colocan al final de la misma:

##

```python
print(milista)
milista.append('hola')
print(milista)
```

---

    ['abcd', 786, 2.23, 'energia', 70.2]
    ['abcd', 786, 2.23, 'energia', 70.2, 'hola']


## <font color="yellow"> Diccionarios</font>

Los diccionarios de python son de tipo tabla-hash.

Funcionan como arrays asociativos y consisten en pares *clave-valor*.

##
Una clave de diccionario puede ser casi cualquier tipo de python, pero suelen ser números o cadenas. 

Los valores, por otra parte, pueden ser cualquier objeto arbitrario de python.

##
Los diccionarios están encerrados por llaves $\{ \; \}$ y los valores se pueden asignar y acceder mediante llaves cuadradas $[ \; ]$.

##
```python
fisicos = dict()

fisicos ={
    1 : "Eistein",
    2 : "Bohr",
    3 : "Pauli",
    4 : "Schrodinger",
    5 : "Hawking"
}

print(fisicos)
print (fisicos.keys())
print (fisicos.values())
fisicos["6"] = "Planck"    #agrega un nuevo elemento al diccionario, tanto su clave como valor
print(fisicos)
```

---

    {1: 'Eistein', 2: 'Bohr', 3: 'Pauli', 4: 'Schrodinger', 5: 'Hawking'}
    dict_keys([1, 2, 3, 4, 5])
    dict_values(['Eistein', 'Bohr', 'Pauli', 'Schrodinger', 'Hawking'])
    {1: 'Eistein', 2: 'Bohr', 3: 'Pauli', 4: 'Schrodinger', 5: 'Hawking', '6': 'Planck'}


## Regla para los identificadores

Los identificadores son nombres que hacen referencia a los objetos que componen un programa: **constantes**, **variables**, **funciones**, etc.

##
Reglas para construir identificadores:

- El primer carácter debe ser una letra o el carácter de subrayado (guión bajo)
- El primer carácter puede ir seguido de un número variable de dígitos numéricos, letras o carácteres de subrayado.
- No pueden utilizarse espacios en blanco, ni símbolos de puntuación.
- En python se distingue  de las mayúsculas y minúsculas.


## Palabras reservadas

No pueden utilizarse palabras reservadas del lenguaje.

|No usar                                        |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|del    |for    |is     |raise  |assert |elif   |
|from   |lamda  |return |break  |else   |global |
|not    |try    |class  |except |if     |or     |
|while  |continue|exec  |import |pass   |yield  |
|def    |finally|in     |print  |del    |system |
