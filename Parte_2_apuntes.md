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


