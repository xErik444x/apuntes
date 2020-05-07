# MODULO 5
+ Módulos de Python.
+ La forma en que los módulos se unen para formar paquetes.
+ El concepto de una excepción y su implementación en Python, incluida la instrucción try-except, con sus aplicaciones y la instrucción raise.
+ Cadenas y sus métodos específicos, junto con sus similitudes y diferencias en comparación con las listas.
  

## ¿Qué es un módulo?

> Son porciones de codigos creados por programadores para ahorrar tiempo y usabilidad.

## ¿Cómo hacer uso de un módulo?

+ El primero (probablemente el más común) ocurre cuando se desea utilizar un módulo ya existente, escrito por otra persona o creado por el programador mismo en algún proyecto complejo: en este caso, se considera al programador como el usuario del módulo.
+ El segundo ocurre cuando se desea crear un nuevo módulo, ya sea para uso propio o para facilitar la vida de otros programadores: aquí eres el proveedor del módulo.
  
## Importando un modulo

> Para que un modulo funcione, hace falta importarlo, ej:

    import nombredelmodulo
    import math
    import modulo1,modulo2,modulo3
    import math
    print(math.sin(math.pi/2))

## Namespace
>Un namespace es un espacio (entendido en un contexto no físico) en el que existen algunos nombres y los nombres no entran en conflicto entre sí (es decir, no hay dos objetos diferentes con el mismo nombre). 

+ Dentro de un determinado namespace, cada nombre debe permanecer único.

## Importando un metodo con diferentes namespaces

        import math

        def sin(x):
            if 2 * x == pi:
                return 0.99999999
            else:
                return None

        pi = 3.14

        print(sin(pi/2))
        print(math.sin(math.pi/2))
        #0.99999999
        #1.0

## Palabras claves al importar

+ from modulo import *
+ import modulo
+ import modulo as mod
+ from math import pi as PI, sin as sine


## Como ver las funciones o nombres de entidades de un modulo

        import math

        for name in dir(math):
            print(name, end="\t")


## Modulo Random

        from random import random

        print(random())

## Modulo para ver datos del SO
        from platform import platform

        print(platform()) #windows x 

        from platform import system

        print(system()) #windows
---
        from platform import machine

        print(machine()) #x86
---
        from platform import processor

        print(processor()) #i5


# palabras claves de un modulo

+ `__name__` se utiliza para saber si el modulo es ejecutado como modulo o como archivo principal
        
        if __name__ == "main":
            soy el archivo principal
        else: # (retorna el nombre del modulo)
            soy un modulo

## Paquetes y modulos

![Paquete](https://raw.githubusercontent.com/xErik444x/apuntesPython/master/img/paquete.png)

>Aspectos importantes:

+ Un módulo es un contenedor lleno de funciones
+ Crear muchos módulos puede causar desorden
+ un paquete: en el mundo de los módulos, un paquete juega un papel similar al de una carpeta o directorio en el mundo de los archivos.
  
## ¿Cómo entrar a una carpeta que contiene el modulo?

    #en el main
    from sys import path
    path.append('..\\modules')
    import modulo


## Try and except

+ La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción y Python comienza a buscar una solución.
+ La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal ç
+ si se genera una excepción dentro del bloque anterior try, fallará aquí, entonces el código ubicado después de la palabra clave except debería proporcionar una reacción adecuada a la excepción planteada.
+ Se regresa al nivel de anidación anterior, es decir, se termina la sección try-except.

        try:
                :
                :
        except:
                :
                :


                BaseException
                        ↑
                Exception
                        ↑
                ArithmeticError
                        ↑
                ZeroDivisionError

        try:
        y = 1 / 0
        except ZeroDivisionError:
        print("¡División entre Cero!")
        except ArithmeticError:
        print("¡Problema aritmético!")

        print("FIN.")

## Funcion raise 

> Esta funcion lo que hace es generar una excepcion de diferentes tipos, estos son definidos por el programador:

        def badFun(n):
    raise ZeroDivisionError

        try:
        badFun(0)
        except ArithmeticError:
        print("¿Que pasó? ¿Un error?")

        print("FIN.")


## Valor unicode o Ascii
> se puede saber empleando la función: ord("a")
> Se puede saber a que corresponde un numero en ascii o unicode con : chr(97)

## Indexando cadenas

                exampleString = 'hola'

                for ix in range(len(exampleString)):
                print(exampleString[ix], end=' ')

                #h o l a

## Haciendo un slice a una cadena

                alpha = "abdefg"

                print(alpha[1:3]) #bd
                print(alpha[3:]) #efg
                print(alpha[:3]) #abd
                print(alpha[3:-2]) #e
                print(alpha[-3:4]) #e
                print(alpha[::2]) #adf
                print(alpha[1::2]) #beg

## Comprobacion de valor dentro de un String

                alpfabeto = "abcdefghijklmnopqrstuvwxyz"

                print("f" in alpfabeto) # True

> las cadenas ***NO SON LISTAS***, por ende, no aceptan metodos del tipo ***del,insert o append***

## Funcion min()

        print(min("aAbByYzZ"))
> Lo que hace es buscar el menor en la tabla ascii "A"

## Funcion max()

        print(max("aAbByYzZ"))
> Lo que hace es buscar el mayor en la tabla ascii "z"

## Metodo index()

> busca la secuencia desde el principio, para encontrar el primer elemento del valor especificado en su argumento.

        print("aAbByYzZaA".index("b")) # 2

## Convertir texto a lista y metodo count()

> Convertir texto a lista: list("abcabc")
> Contar las veces que aparece x cosa en la lista: "abcabc".count("b") # 2

## Metodo capitalize()

> Convierte toda la cadena segun la primera letra o caracter.
+ Si existe la primer letra, entonces, la hace mayusculas y las demas minisculas ej
+ - capitalize("aBCD") # Abcd

## método center()

> Su función es centrar el texto, ej:

        print('[' + 'alfa'.center(10) + ']') # [   alfa   ]
        print('[' + 'alfa'.center(30,"*") + ']') # [*************alfa*************]
+ El centrado se realiza realmente al agregar algunos espacios antes y después de la cadena.

## método endswith()

> Comprueba si la cadena termina en un valor definido, ej:

        if "casa".endswith("sa"):
        print("si, casa termina en 'sa'")
        else:
        print("no, casa no termina en 'sa'")

## método find()

> Busca la posicion de una cadena dentro de otra, si no la encuentra devuelve el valor "-1", funciona casi como el metodo index.
        print("Eta".find("ta")) # 1
        print("Eta".find("asdasdas")) # -1

## Métodos para comprobar si la cadena contiene letras y/o numeros

> isalnum() Devuelve True si la cadena contiene numeros, no importa si tiene letras. "ads12".isalnum() #True
> isalpha() da True si solo contiene letras "ads12".isalnum() #False
> isdigit() Busca solo digitos "123".isalnum() #True

## Métodos para comprobar cosas en las cadenas xd

> islower() Solo acepta letras minusculas
> isspace() Comprueba si hay espacios
> isupper() Comprueba si hay mayusculas

## Método join()
> Realiza una union, toma como argumento una lista(que no sea de varias dimensiones) y crea una apartir de este argumento, ej:
        print("-".join(["omicron", "pi", "rho"])) (Se toma como primer argumento el separador y luego va el .join.)

## Método lower()
> Transforma el String en minusculas.
+ - `print("SiGmA=60".lower()) # sigma=60`
  
## Método lstrip()
>  devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.
+ - `print("        tau ".lstrip() + "]")` # "tau ]"

> Tambien acepta parametros, en este caso, eliminaria de la cadena, todo lo que coincida con el parametro:
+ - `print("www.erikschwerdt.ml".lstrip("w."))` # erikschwerdt.ml
+ - `print("pythoninstitute.org".lstrip(".org"))` # pythoninstitute.org (no puede reemplazar la ultima parte del string)

## Método replace()
> Reemplaza en el String lo que le pasemos por argumento:
+ - `print("Que onda prros !".replace("onda", ""))` #Que prros!
+ + - `print("Que onda prros !".replace("onda", "feos"))` #Que feos prros!
> El 3er argumento se utiliza para las veces que queremos reemplazar
+ - `print("This is it!".replace("is", "are", 2))` # thare are it!

## Método rfind()
> Hace lo mismo que el metodo find(), pero en reversa, va del ultimo al primero. (la r) es de reverse

## método rstrip()
> Hace lo mismo que el metodo lstrip(), pero en reversa, ej:
+ - `print("cisco.com".rstrip(".com"))` # cis