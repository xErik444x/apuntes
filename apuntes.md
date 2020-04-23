# apuntes de python
## ¿Qué es Python?
>Python es un lenguaje de programación de alto nivel, interpretado, orientado a objetos y de uso generalizado con semántica dinámica, que se utiliza para la programación de propósito general.

## objetivos de Python
+ Un lenguaje fácil e intuitivo tan poderoso como los de los principales competidores.
+ De código abierto, para que cualquiera pueda contribuir a su desarrollo.
+ El código que es tan comprensible como el inglés simple.
+ Adecuado para tareas cotidianas, permitiendo tiempos de desarrollo cortos.

## ¿Dónde podemos ver a Python en acción?
+ Servicios de Internet como motores de búsqueda
+ Almacenamiento en la nube y herramientas
+ Redes sociales, etc

## ¿Qué es una función?
* Un efecto.
* Un resultado.

## pasos de  una función
* Primero, Python comprueba si el nombre especificado es legal
* En segundo lugar, Python comprueba si los requisitos de la función para el número de argumentos le permiten invocar la función de esta manera
* Tercero, Python deja el código por un momento y salta dentro de la función
* Cuarto, la función ejecuta el código
* Finalmente, Python regresa al código

## Literales
> Un literal se refiere a datos cuyos valores están determinados por el literal mismo.

## Enteros
> Enteros, es decir, aquellos que no tienen una parte fraccionaria.

Python no permite escribir "." en lo numeros, en lugar de eso se puede poner "_" ej: "2_020" o "2020"

### números octales y hexadecimales
    Si un numero entero esta precedido por un código 0O o 0o (cero-o), el numero será tratado como un valor octal. Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.

> 0o123 es un número octal con un valor (decimal) igual a 83.

> La función print() realiza la conversión automáticamente.

    La segunda convención nos permite utilizar números en hexadecimal. Dichos números deben ser precedidos por el prefijo 0x o 0X (cero-x).

> 0x123 es un número hexadecimal con un valor (decimal) igual a 291

## Floats
> 4.0 0.4 4.

    Por otro lado, no solo el punto hace que un número sea flotante. Se puede utilizar la letra "e"

> 3 x 10 elevado a 8 = 3E8
   
    La letra E (también se puede utilizar la letra minúscula e - proviene de la palabra exponente) 

* El exponente (el valor después de la E) debe ser un valor entero.
* La base (el valor antes de la E) puede o no ser un valor entero.

### Codificando Flotantes
> 6.62607 x 10-34 = 6.62607E-34

`print(0.0000000000000000000001)` "1e-22"

    Python siempre elige la presentación más corta del número, y esto se debe de tomar en consideración al crear literales.

## Strings
`print("Me gusta \"Monty Python\"")` = 'Me gusta  "Monty Python"'


## Numeros y matematicas
### Operadores aritméticos
> exponenciación
> 
    Un signo de ** (doble asterisco) es un operador de exponenciación (potencia)
    2 ** 3 = 8
> división entera
    Un símbolo de // (doble diagonal) es un operador de división entera.
    los resultados siempre son redondeados.
    y si un numero es flotante da resultado como float.
    el redondeo siempre va hacia abajo.

> (módulo) %

    El resultado de la operación es el residuo que queda de la división entera.

## Operadores y sus enlaces
### exponenciación
    "***" este va de derecha a izquierda, rompienda la norma de lectura normal de python
`print(2 ** 2 ** 3)` 2 ** 3 → 8; 2 ** 8 → 256


## función input()
 > Una cadena que contiene todos los caracteres que el usuario introduce desde el teclado. No es un entero ni un flotante.

 `x = input("quien sos?...")`
 
 `print("que nombre tan feo...",x)`


## Decisiones y operadores
> igual a (==)  |  no es igual a (!=)

> operador > (mayor que)

> `>= (mayor o igual que) | <= (menor o igual que)`

__IF:__

    if climaEsBueno:
        irACaminar()
    else:
        irAlCine()
    almorzar() 

>palabra clave de Python: elif (elseIf mas corto)
   
    if climaBueno:
        iraCaminar()
    elif hayBoletosDisponibles:
        IralCine()
    elif mesasLibres:
        almorzar()
    else:
        jugarAjedrezEnCasa() 


## Bucles

    línea 01  numeroMayor = -999999999
    línea 02  numero = int(input())
    línea 03  if numero == -1:
    línea 04  print(numeroMayor)
    línea 05  exit()
    línea 06  if numero > numeroMayor:
    línea 07  numeroMayor = numero
    línea 08  vaya a la línea 02

 >python trae una palabra clave para saber cual es el mayor de todos, lo mismo para el menor:

    numeroMayor = max(numero1,numero2,numero3)
    numeroMenor =min(numero1,numero2,numero3)
  
> Impresion multilinea

    """
    +==================================+
    | Bienvenido a mi juego, muggle!   |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """
>While

    while condicion:
        hacer x cosa

 >For

    for i in range (100):
        #hacer algo()
        pass #(Es obligatorio poner algo dentro, el pass no hace nada.)

la instruccion "range()" acepta 3 parametros, los dos primeros son de donde hasta donde va a ir el for, el tercero es de a cuantos pasos, ej:
`for in range(2,11,2):`(anda del 2 al 10 pasando de 2 en 2) `range(start, stop, step)`

Si el range no lleva a ningun lado no se va a ejecutar tipo: `range(1,1)`


## break y continue
> Palabras claves reservadas.

>Break: Sale del ciclo inmediatamente

    for i in range(1,6):
        if i == 3:
            break
        print("Dentro del ciclo.", i)
    print("Fuera del ciclo.")
    #cuando sea 3 termina el ciclo

>Continue: 

    for i in range(1,6):
        if i == 3:
            continue
        print("Dentro del ciclo.", i)
    print("Fuera del ciclo.")
    #cuando sea 3 se saltea el contenido del if pero sigue en el bucle. Es como si hubiera llegado al final de ese if.


## AND
`contador > 0 and valor == 100 `
|Argumento A|Argumento B|A y B|
|---|---|---|
|False|False|False|
|False|True|False|
|True|False|False|
|True|True|True|

## OR
 >prioridad más baja que and.
 `contador > 0 or valor == 100 `

    se ejecuta siempre que uno sea verdadero
|Argumento A|Argumento B|A or B|
|---|---|---|
|False|False|False|
|False|True|True|
|True|False|True|
|True|True|True|


## NOT
>operador unario que realiza una negación lógica

    Su prioridad es muy alta: igual que el unario + y -

|Argumento A|not A|
|---|---|
|False|True|
|True|False|


## Valores lógicos vs. bits individuales

    Los operadores lógicos toman sus argumentos como un todo, independientemente de cuántos bits contengan. Los operadores solo conocen el valor: cero (cuando todos los bits se restablecen) significa False; no cero (cuando se establece al menos un bit) significa True.

## Operadores bitwise

 * &  (ampersand) - conjunción a nivel de bits.
 * |  (barra vertical) - disyunción a nivel de bits.
 * ~  (tilde) - negación a nivel de bits.
 * ^  (signo de intercalación) - exclusivo a nivel de bits o (xor).

* &  requieres exactamente dos  1  s para proporcionar  1  como resultado.
* |  requiere al menos un  1  para proporcionar  1  como resultado.
* ^  requiere exactamente un  1  para proporcionar  1  como resultado.


> Operaciones bitwise (&, |, y ^)

| Arg A | Arg B | A `&` B | A `|` B | A `^` B |
|:---:|:---:|:---:|:---:|:---:|
|0|0|0|0|0|
|0|1|0|1|1|
|1|0|0|1|1|
|1|1|1|1|0|

 >(~)

|Arg A `|`|~A|
|:-:|:-:|
|0|1|
|1|0|





---
## Prioridades

| Prioridad | Operador |
|:---:|---|
|1|+, - (unario)|
|2|**|
|3|*, /, %|
|4|+, -	(binario)|
|5|<, <=, >, >=|
|6|==, !=|










<br>

---

<h1> Let's code! </h1>

## Print in console:
> `print("hello world")`

If I write a file, I can run it using "F5"

> `print("La Witsi Witsi Arañar" , "subió" , "a su telaraña.")`
"La Witsi Witsi Arañar subió a su telaraña."

* Una función print() invocada con más de un argumento genera la salida en una sola línea.
* La función print() pone un espacio entre los argumentos emitidos por iniciativa propia.

> La función print() tiene dos argumentos de palabras clave que se pueden utilizar para estos propósitos. El primero de ellos se llama end

`print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")` "Mi nombre es Python. Monty Python."
>el 'end=" "' Establece el caracter que se envia al final, ejemplo 'end= "\n"'

`print("Mi", "nombre", "es", "Monty", "Python.", sep="-")` "Mi-nombre-es-Monty-Python."

`print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("-hola monty.")` 
> Mi_nombre_es*Monty*Python.*
> 
> -hola monty.

`print("Fundamentos","Programación","en",sep="***",end="...")
print("Python")`
> Fundamentos *** Programación*** en...Python

`print("    *","   * *","  *   *"," *     *","***   ***","  *   *","  *   *","  *****", sep="\n")`
> flecha.

`print('"Estoy"', '""aprendiendo""','"""Python"""')`

`print("\"Estoy\"","\"\"aprendiendo\"\"","\"\"\"Python\"\"\"", sep="\n")`

    "Estoy"
    ""aprendiendo""
    """Python"""

---
## Laboratorio variables 
    Crear las variables: juan, maria, y adan.
    Asignar valores a las variables. El valor debe de ser igual al numero de manzanas que cada quien tenía.
    Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma.
    Después se debe crear una nueva variable llamada totalManzanas y se debe igualar a la suma de las tres variables anteriores.
    Imprime el valor almacenado en totalManzanas en la consola.

> `juan = 3`

> `maria = 5`

> `adan = 6`

`print(juan,maria,adan, sep=",")`

`totalManzanas = juan + maria + adan`

`print ("total de manzanas:", totalManzanas)`

## Fin Laboratorio variables
___
