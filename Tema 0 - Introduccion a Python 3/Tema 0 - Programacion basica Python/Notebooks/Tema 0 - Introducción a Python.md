
# Operadores aritméticos
## Python como calculadora

Una vez abierta la sesión en $\texttt{python}$, podemos aprovechar al máximo este lenguaje: contamos con una calculadora a la mano, sólo hay que ir escribiendo las operaciones en la línea de comandos.


```python
3+200
```




    203




```python
3/4
```




    0.75




```python
3.0/4.0
```




    0.75




```python
3//4
```




    0




```python
4//3
```




    1




```python
4/3
```




    1.3333333333333333




```python
5.0 / 10 * 2 + 5
```




    6.0



¿por qué obtenemos este resultado??


```python
5.0 / (10 * 2 + 5)
```




    0.2



Como podemos ver, el uso de paréntesis en las expresiones tiene una particular importancia sobre la manera en que se evalúan las expresiones

Podemos elevar un número a una potencia en particular


```python
2**3**2
```




    512



Vemos que elevar a una potencia, la manera en que se ejecuta la expresión se realiza en un sentido en particular: de derecha a izquierda


```python
(2**3)**2
```




    64



El uso de paréntesis nos indica que la expresión contenida dentro de ellos, es la que se evalúa primero, posteriormente se sigue la regla de precedencia de operadores

El operador módulo $(\%)$ nos devuelve el residuo del cociente


```python
17%3
```




    2



# Tabla de operadores

 <table>
     <caption><span style="color:red">Precedencia en los operadores aritméticos</span></caption>
  <tr background-color="black">
    <th>Operador</th>
    <th>Operación</th>
    <th>Ejemplo</th>
    <th>Resultado</th>
  </tr>
  <tr>
   
    <td>$**$</td>
    <td>Potencia</td>
    <td>$2**3$ </td>
    <td>$8$ </td>
  </tr>
  <tr>
    <td>$*$</td>
    <td>Multiplicación</td>
    <td>$7*3$</td>
    <td>$21$</td>
  </tr>
  <tr>
    <td>$/$</td>
    <td>División</td>
    <td>$10.5/2$</td>
    <td>$5.25$</td>
  </tr>
  <tr>
    <td>$//$</td>
    <td>División entera</td>
    <td>$10.5//2$</td>
    <td>$5.0$</td>
  </tr>
  <tr>
    <td>$+$</td>
    <td>Suma</td>
    <td>$3+4$</td>
    <td>$7$</td>
  </tr>
  <tr>
    <td>$-$</td>
    <td>Resta</td>
    <td>$6-8$</td>
    <td>$-2$</td>
  </tr>
  <tr>
    <td>$\%$</td>
    <td>Módulo</td>
    <td>$15\%6$</td>
    <td>$3$</td>
  </tr>
</table>

# Precedencia de los operadores artiméticos

1. Las expresiones contenidas dentro de pares de paréntesis son evaluadas primero. En el caso de expresiones con paréntesis anidados, los operadores en el par de paréntesis más interno son aplicados primero.
2. Las operaciones de exponentes son aplicadas después. Si una expresión contiene muchas operaciones de exponentes, los operadores son aplicados de derecha a izquierda.
3. La multiplicación, división y módulo son las siguientes en ser aplicadas. Si una expresión contiene muchas multiplicaciones, divisiones u operaciones de módulo, los operadores se aplican de izquierda a derecha.
4. Suma y resta son las operaciones que se aplican por último. Si una expresión contiene muchas operaciones de suma y resta, los operadores son aplicados de izquierda a derecha. La suma y resta tienen el mismo nivel de precedencia.


# Operadores relacionales

Se comparan dos (o más expresiones) mediante un operador, el tipo de dato que devuelve es lógico: $\textbf{True}$ o $\textbf{False}$, que también tienen una representación de tipo numérico:
- $\textbf{True}$ = 1
- $\textbf{False}$ = 0


```python
1 + 2 > 7- 3
```




    False




```python
1 < 2 < 3
```




    True




```python
1 > 2 == 2 < 3
```


```python
1 > (2 ==  2) <3
```




    False




```python
3 > 4 < 5
```




    False




```python
1.0 / 3 < 0.3333
```




    False




```python
5.0 / 3 >= 11 /7.0
```




    True




```python
2**(2. /3) < 3**(3./4)
```




    True



## Tabla de operadores relacionales

<div class="centrado">
<table width="50%">
     <caption><span style="color:red">Operadores relacionales</span></caption>
  <tr background-color="black">
    <th>Operador</th>
    <th>Operación</th>
    <th>Ejemplo</th>
    <th>Resultado</th>
  </tr>
  <tr>
    <td class="centrado">$==$</td>
    <td>Igual a</td>
    <td>$4==5$</td>
    <td>$\texttt{False}$</td>
  </tr>
  <tr>
    <td>$!=$</td>
    <td>Diferente de</td>
    <td>$2!=3$</td>
    <td>$\texttt{True}$</td>
  </tr>
  <tr>
    <td>$<$</td>
    <td>Menor que</td>
    <td>$10<4$</td>
    <td>$\texttt{False}$</td>
  </tr>
  <tr>
    <td>$>$</td>
    <td>Mayor que</td>
    <td>$5>-4$</td>
    <td>$\texttt{True}$</td>
  </tr>
  <tr>
    <td>$<=$</td>
    <td>Menor o igual que</td>
    <td>$7<=7$</td>
    <td>$\texttt{True}$</td>
  </tr>
  <tr>
    <td>$>=$</td>
    <td>Mayor o igual que</td>
    <td>$3.5 >= 10$</td>
    <td>$\texttt{False}$</td>
  </tr>
</table>
</div>


##  Operadores boleanos

En el caso del operador boleano $\texttt{and}$ y el operador $\texttt{or}$ evalúan una expresión compuesta por dos (o más términos), en ambos operadores se espera que cada término tenga el valor de <font color='blue'>$\texttt{True}$</font>, en caso de que esto ocurra, el valor que devuelve la evaluación, es <font color='blue'>$\texttt{True}$</font>, como se verá en la tabla de verdad, se necesita una condición particular para que el valor que devuelva la comparación, sea <font color='red'>$\texttt{False}$</font>.

<table width="50%">
     <caption><span style="color:red">Operadores boleanos</span></caption>
  <tr>
    <th>Operador</th>
    <th>Operación</th>
    <th>Ejemplo</th>
    <th>Resultado</th>
  </tr>
  <tr>
    <td>$\texttt{and}$</td>
    <td>Conjunción</td>
    <td>$\texttt{False and True}$</td>
    <td>$\texttt{False}$</td>
  </tr>
  <tr>
    <td>$\texttt{or}$</td>
    <td>Disyunción</td>
    <td>$\texttt{False or True}$</td>
    <td>$\texttt{True}$</td>
  </tr>
    <tr>
    <td>$\texttt{not}$</td>
    <td>Negación</td>
    <td>$\texttt{not True}$</td>
    <td>$\texttt{False}$</td>
  </tr>
  </table>

## Tabla de verdad de los operadores boleanos

<table width="50%">
     <caption><span style="color:red">Tabla de verdad</span></caption>
  <tr>
    <th>$\texttt{A}$</th>
    <th>$\texttt{B}$</th>
    <th>$\texttt{A and B}$</th>
    <th>$\texttt{A or B}$</th>
    <th>$\texttt{not A}$</th>
  </tr>
  <tr>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
  </tr>
  <tr>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
  </tr>
  <tr>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
  </tr>
  <tr>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=red>$\texttt{False}$</font></td>
    <td><font color=blue>$\texttt{True}$</font></td>
  </tr>
  </table>

# Tipos de variables

Las variables en $\texttt{python}$ sólo son ubicaciones de memoria reservadas para almacenar valores. Esto significa que cuando se crea una variable, se reserva un poco de espacio disponible en la memoria.

Basándose en el tipo de datos de una variable, el intérprete asigna memoria y decide qué se puede almacenar en la memoria reservada. Por lo tanto, al asignar diferentes tipos de datos a las variables, se pueden almacenar **enteros**, **decimales** o **caracteres (cadenas)** en estas variables.



## Asignando valores a variables

Las variables de $\texttt{python}$ no necesitan una declaración explícita para reservar espacio de memoria. La declaración ocurre automáticamente cuando se asigna un valor a una variable. **El signo igual (=) se utiliza para asignar valores a las variables*.

El término a la izquierda del operador = es el *nombre de la variable* y el término a la derecha del operador = es el *valor almacenado* en la variable.


```python
contador = 100          # Asignacion de tipo entero
distancia = 1000.0      # De punto flotante
nombre = "Chucho"       # Una cadena de caracteres

print (contador)
print (distancia)
print (nombre)
```

    100
    1000.0
    Chucho


## Asignación múltiple de valores

En $\texttt{python}$  podemos asignar un valor único a varias variables simultáneamente.


```python
A = b = c = 1
print (A)
print (b)
print (c)
```

    1
    1
    1


En el ejemplo, se crea un objeto entero con el valor $1$, y las tres variables se asignan a la misma ubicación de memoria. 

También puede asignar varios objetos a varias variables.


```python
A, b, c = 1, 2, "Alicia"
print (A)
print (b)
print (c)
```

    1
    2
    Ana


Aquí, dos objetos enteros con valores $1$ y $2$ se asignan a las variables $A$ y $b$ respectivamente, y un objeto de cadena con el valor **Alicia** se asigna a la variable $c$.

## Tipos de Datos Estándar

Los datos almacenados en la memoria pueden ser de varios tipos. Por ejemplo, la edad de una persona se almacena como un valor numérico y su dirección se almacena como caracteres alfanuméricos.

En $\texttt{python}$ se cuenta con varios tipos de datos estándar que se utilizan para definir las operaciones posibles entre ellos y el método de almacenamiento para cada uno de ellos.

Los tipos de datos son cinco:
- <font color="blue"> Números</font>.
- <font color="blue"> Cadena</font>.
- <font color="blue"> Lista</font>.
- <font color="blue"> Tupla</font>.
- <font color="blue"> Diccionario</font>.

### Números 

Los tipos de datos numéricos almacenan valores numéricos. Los objetos numéricos se crean cuando se les asigna un valor.


```python
Var1 = Var2 = 10
print (Var1)
print (Var2)
```

    10
    10


También se puede eliminar la referencia a un objeto numérico utilizando la sentencia <font color="blue">$\texttt{del}$</font>.

La sintaxis de la sentencia del es:

$del$  $var1 [, var2 [, var3 [...., varN]]]]$

Se puede eliminar un solo objeto o varios objetos utilizando la sentencia $\texttt{del}$

Por ejemplo:

$del$ $var$

$del$ $variable1$, $variable2$

En $\texttt{python}$ se soportan tres tipos numéricos diferentes:

1. <font color="blue">Int (enteros con signo)</font>
2. <font color="blue">Flotante (valores reales de punto flotante)</font>
3. <font color="blue">Complejos (números complejos)</font>

Un número complejo consiste en un par ordenado de números reales de coma flotante denotados por
$$x + yj$$
donde $x$ e $y$ son números reales, $yj$ es la unidad imaginaria. Todos los enteros en $\texttt{python 3}$ se representan como enteros largos. Por lo tanto, no hay ningún tipo de número por separado.

<table width="50%" style="align:center";>
     <caption><span style="color:red">Ejemplos de tipo de números</span></caption>
  <tr>
    <th>$\texttt{int}$</th>
    <th>$\texttt{float}$</th>
    <th>$\texttt{complex}$</th>
  </tr>
  <tr>
    <td>$\texttt{10}$</td>
    <td>$\texttt{0.0}$</td>
    <td>$\texttt{3.14j}$</td>
  </tr>
  <tr>
    <td>$\texttt{100}$</td>
    <td>$\texttt{15.20}$</td>
    <td>$\texttt{45.j}$</td>
  </tr>
  <tr>
    <td>$\texttt{100}$</td>
    <td>$\texttt{15.20}$</td>
    <td>$\texttt{45.j}$</td>
  </tr>
  <tr>
    <td>$\texttt{080}$</td>
    <td>$\texttt{32.3+e18}$</td>
    <td>$\texttt{0.876j}$</td>
  </tr>
  <tr>
    <td>$\texttt{-0490}$</td>
    <td>$\texttt{-90.}$</td>
    <td>$\texttt{-.645+0j}$</td>
  </tr>
  <tr>
    <td>$\texttt{-0x260}$</td>
    <td>$\texttt{-32.54e100}$</td>
    <td>$\texttt{3e+26j}$</td>
  </tr>
  <tr>
    <td>$\texttt{0x69}$</td>
    <td>$\texttt{70.2-E12}$</td>
    <td>$\texttt{4.53e-7j}$</td>
  </tr>
 </table>

### Cadenas 

Las cadenas en $\texttt{python}$ se identifican como un conjunto contiguo de caracteres representados en las comillas. Con $\texttt{python}$ se permite cualquier par de comillas simples o dobles.

Los subconjuntos de cadenas pueden ser tomados usando el operador de corte ($[\;]$ y $[:]$) con índices comenzando en $0$ al inicio de la cadena hasta llegar a $-1$ al final de la misma.

El signo más ($+$) es el operador de concatenación de cadenas y el asterisco ($*$) es el operador de repetición.


```python
cadena = 'Hola Mundo!'

print (cadena)          # Presenta la cadena completa
print (cadena[0])       # Presenta el primer caracter de la cadena
print (cadena[2:5])     # Presenta los caracteres de la 3a a la 5a posicion
print (cadena[2:])      # Presenta la cadena que inicia a partir del 3er caracter
print (cadena * 2)      # Presenta dos veces la cadena
print (cadena + "PUMAS") # Presenta la cadena y concatena la segunda cadena
```

    Hola Mundo!
    H
    la 
    la Mundo!
    Hola Mundo!Hola Mundo!
    Hola Mundo!PUMAS


### Listas

Las listas es el tipo de dato más versátil de los tipos de datos compuestos de $\texttt{python}$.

Una lista contiene elementos separados por comas y entre corchetes ($[ \; ]$). En cierta medida, las listas son similares a los arreglos (arrays) en el lenguaje C. Una de las diferencias entre ellos es que todos los elementos pertenecientes a una lista pueden ser de tipo de datos diferente.

Los valores almacenados en una lista se pueden acceder utilizando el operador de división ($[ \; ]$ y $[:]$) con índices que empiezan en $0$ al principio de la lista y opera hasta el final con $-1$.

El signo más ($+$) es el operador de concatenación de lista y el asterisco ($*$) es el operador de repetición.


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

    ['abcd', 786, 2.23, 'salmon', 70.2]
    abcd
    [786, 2.23]
    [2.23, 'salmon', 70.2]
    [123, 'pizza', 123, 'pizza']
    ['abcd', 786, 2.23, 'salmon', 70.2, 123, 'pizza']


### Tuplas 

Una tupla es otro tipo de datos de secuencia que es similar a la lista.

Una tupla consiste en un número de valores separados por comas. Sin embargo, a diferencia de las listas, las tuplas se incluyen entre paréntesis.

La principal diferencia entre las listas y las tuplas son:
1. Las listas están entre corchetes $[\;]$ y sus elementos y tamaño pueden cambiarse.
2. Las tuplas están entre paréntesis $(\;)$ y <u>no se pueden actualizar</u>.

Las tuplas pueden ser consideradas como listas de sólo lectura.


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

    ('abcd', 786, 2.23, 'arena', 70.2)
    abcd
    (786, 2.23)
    (2.23, 'arena', 70.2)
    (123, 'playa', 123, 'playa')
    ('abcd', 786, 2.23, 'arena', 70.2, 123, 'playa')


El siguiente código es inválido con la tupla, porque intentamos actualizar una tupla, que la acción no está permitida. El caso es similar con las listas.


```python
mitupla = ( 'abcd', 786 , 2.23, 'edificio', 70.2  )
milista = [ 'abcd', 786 , 2.23, 'energia', 70.2  ]
mitupla[2] = 1000    # Sintaxis invalida para la tupla
milista[2] = 1000     # Sintaxis invalida para la lista
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-a99f473d7b8f> in <module>()
          1 mitupla = ( 'abcd', 786 , 2.23, 'edificio', 70.2  )
          2 milista = [ 'abcd', 786 , 2.23, 'energia', 70.2  ]
    ----> 3 mitupla[2] = 1000    # Sintaxis invalida para la tupla
          4 milista[2] = 1000     # Sintaxis invalida para la lista


    TypeError: 'tuple' object does not support item assignment


Pero en la lista podemos agregar nuevos elementos que se colocan al final de la misma:


```python
print(milista)
milista.append('hola')
print(milista)
```

    ['abcd', 786, 2.23, 'energia', 70.2]
    ['abcd', 786, 2.23, 'energia', 70.2, 'hola']


### Diccionarios

Los diccionarios de $\texttt{python}$ son de tipo tabla-hash.

Funcionan como arrays asociativos y consisten en pares *clave-valor*.

Una clave de diccionario puede ser casi cualquier tipo de $\texttt{python}$, pero suelen ser números o cadenas. Los valores, por otra parte, pueden ser cualquier objeto arbitrario de $\texttt{python}$.

Los diccionarios están encerrados por llaves $\{ \; \}$ y los valores se pueden asignar y acceder mediante llaves cuadradas $[ \; ]$.


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

    {1: 'Eistein', 2: 'Bohr', 3: 'Pauli', 4: 'Schrodinger', 5: 'Hawking'}
    dict_keys([1, 2, 3, 4, 5])
    dict_values(['Eistein', 'Bohr', 'Pauli', 'Schrodinger', 'Hawking'])
    {1: 'Eistein', 2: 'Bohr', 3: 'Pauli', 4: 'Schrodinger', 5: 'Hawking', '6': 'Planck'}


## Regla para los identificadores

Los identificadores son nombres que hacen referencia a los objetos que componen un programa: **constantes**, **variables**, **funciones**, etc.

Reglas para construir identificadores:
- El primer carácter debe ser una letra o el carácter de subrayado (guión bajo)
- El primer carácter puede ir seguido de un número variable de dígitos numéricos, letras o carácteres de subrayado.
- No pueden utilizarse espacios en blanco, ni símbolos de puntuación.
- En $\texttt{python}$ se distingue  de las mayúsculas y minúsculas.
- No pueden utilizarse palabras reservadas del lenguaje.

<table>
<caption><span style="color:red">Lista de palabras reservadas en $\texttt{python}$</span></caption>
<tr>
  <td>$\texttt{del}$</td>
  <td>$\texttt{for}$</td>
  <td>$\texttt{is}$</td>
  <td>$\texttt{raise}$</td>
  <td>$\texttt{assert}$</td>
  <td>$\texttt{elif}$</td>
</tr>
<tr>
  <td>$\texttt{from}$</td>
  <td>$\texttt{lamda}$</td>
  <td>$\texttt{return}$</td>
  <td>$\texttt{break}$</td>
  <td>$\texttt{else}$</td>
  <td>$\texttt{global}$</td>
</tr>
<tr>
  <td>$\texttt{not}$</td>
  <td>$\texttt{try}$</td>
  <td>$\texttt{class}$</td>
  <td>$\texttt{except}$</td>
  <td>$\texttt{if}$</td>
  <td>$\texttt{or}$</td>
</tr>
<tr>
  <td>$\texttt{while}$</td>
  <td>$\texttt{continue}$</td>
  <td>$\texttt{exec}$</td>
  <td>$\texttt{import}$</td>
  <td>$\texttt{pass}$</td>
  <td>$\texttt{yield}$</td>
</tr>
<tr>
  <td>$\texttt{def}$</td>
  <td>$\texttt{finally}$</td>
  <td>$\texttt{in}$</td>
  <td>$\texttt{print}$</td>
  <td>$\texttt{del}$</td>
  <td>$\texttt{system}$</td>
</tr>
</table>


```python

```
