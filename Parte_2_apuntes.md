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