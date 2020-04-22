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
<br>

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

