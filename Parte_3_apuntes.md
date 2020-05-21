# Python orientado a objetos

## ¿Qué es un objeto?

> Una clase (entre otras definiciones) es un conjunto de objetos. Un objeto es un ser perteneciente a una clase.
> Un objeto es una encarnación de los requisitos, rasgos y cualidades asignados a una clase específica. 

## ¿Qué contiene un objeto?

+ Un objeto tiene un nombre que lo identifica de forma exclusiva dentro de su namespace.
+ Un objeto tiene un conjunto de propiedades individuales que lo hacen original, único o sobresaliente (aunque es posible que algunos objetos no tengan propiedades).
+ Un objeto tiene un conjunto de habilidades para realizar actividades específicas, capaz de cambiar el objeto en sí, o algunos de los otros objetos.

> Ejemplo:

        Max es un gato grande que duerme todo el día.
        Nombre del objeto = Max
        Clase de inicio = Gato
        Propiedad = Tamaño (grande)
        Actividad = Dormir (todo el día)

## Encapsulamiento

> nombre que comienza con dos guiones bajos (__) se vuelve privado.

                class Pila:
                def __init__(self):
                        self.__listaPila = []

                objetoPila = Pila()
                print(len(objetoPila.__listaPila)) # va a dar error porque no lo ejecutamos desde la clase, sino desde fuera.