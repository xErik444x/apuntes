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