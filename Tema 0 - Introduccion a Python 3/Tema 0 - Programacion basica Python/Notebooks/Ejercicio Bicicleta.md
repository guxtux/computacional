
# Ejercicio Completo

## Carrera de bicicletas: el efecto de la resistencia al aire.

La bicicleta es una forma muy eficiente de transporte, esto la sabe quien se ha subido a una.

El objetivo con este ejercicio es entender los factores que determinan la velocidad máxima de una bicicleta y estimar esta velocidad para un caso realista. 

##
Comenzaremos ignorando la fricción; se tiene que considerar posteriormente, pero primero vamos a entender cómo lidiar con el caso más simple sin fricción.

##
Partimos con la ecuación de movimiento: con la segunda ley de Newton, que puede escribirse en la forma

$\dfrac{d v}{dt} = \dfrac{F}{m}$


Donde $v$ es la velocidad, $m$ es la masa de la combinación bicicleta-ciclista, $t$ es el tiempo y $F$ es la fuerza sobre la bicicleta que viene del esfuerzo del ciclista (aquí asumiremos que la bicicleta se está moviendo en plano terreno).

##
Manejar debidamente la $F$ es complicado, por la mecánica misma de una bicicleta: ya que la fuerza ejercida por el ciclista se transmite a las ruedas por medio del plato, engranajes, etc.

Esto hace muy difícil obtener una expresión exacta para $F$.

##
Sin embargo, hay otra manera de atacar este problema que evita la necesidad de conocer la fuerza.

Este enfoque alternativo implica formular el problema en términos de la potencia generada por el conductor. 

##
Los estudios fisiológicos de ciclistas de élite de carreras han demostrado que estos atletas son capaces de producir una potencia de salida de aproximadamente 400 watts durante largos períodos de tiempo (1 h)

##
Usando ideas de trabajo-energía podemos reescribir la ecuación anterior como

\begin{equation*}
\dfrac{d E}{d t} = P
\end{equation*}

Donde $E$ es la energía total de la combinación bicicleta-ciclista, y $P$ es la potencia de salida del ciclista.

##
Esto supone implícitamente que se pierde muy poca energía para la fricción en la propia bicicleta, incluiremos otras fuentes de fricción en un momento.

##
Para un recorrido plano toda la energía es cinética, entonces 

$ E = \frac{1}{2}m v^{2} $

por tanto

\begin{equation*}
\dfrac{d E }{dt} = m v \dfrac{d v}{d t}
\end{equation*}

##
Al sustituir en la ecuación anterior

\begin{equation*}
\dfrac{dv }{d t} = \dfrac{P}{m v}
\end{equation*}

Si $P$ es constante, se puede resolver analíticamente.

##
Ordenando los términos


