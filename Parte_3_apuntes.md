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

## Comprobar si un objeto contiene un atributo
> hasattr(objeto,atributo)
                class ClaseEjemplo:
                attr = 1

                print(hasattr(ClaseEjemplo, 'attr'))
                print(hasattr(ClaseEjemplo, 'prop'))

## Algunos nombres de metodos para clases
+ ``__init__``
  - Es el constructor de la clase. 
+ ``__nombre``
  - un método cuyo nombre comienza con '__' está (parcialmente) oculto.

                def __oculto(self)
                obj._conClase__oculto()

+ ``__dict__ ``
  - Muestra las propiedades y metodos de la clase / objeto
+ ``__name__`` y ``__module__``
  - Devuelve el nombre de la clase
  
              class conClase:
                    pass
                print(conClase.__name__) #Error
                obj = conClase()
                print(type(obj).__name__)
+ ``__bases__``
  - Es una tupla, contiene clases (super clases directas para las clases)
  
## Reflexión e introspección

+ **Introspección**, que es la capacidad de un programa para examinar el tipo o las propiedades de un objeto en tiempo de ejecución.
  
+ **Reflexión**, que va un paso más allá, y es la capacidad de un programa para manipular los valores, propiedades y/o funciones de un objeto en tiempo de ejecución.
  
## Herencia
> Cuando python necesita que una clase sea representada por un string (print) llama a un metodo llamado `__str__()`, este puede ser modificado por nosotros:

    class Estrella:
        def __init__(self, nombre, galaxia):
            self.nombre = nombre
            self.galaxia = galaxia

        def __str__(self): # Nuestro propio __str__
            return self.nombre + ' en la ' + self.galaxia

    sol = Estrella("Sol", "Vía Láctea")
    print(sol)

## Herencia: issubclass()
> Para identificar una relación entre dos clases se utiliza `issubclass(ClaseUno, ClaseDos)`

## Herencia: isinstance()
> Para identificar si un objeto proviene de una clase se utiliza: `isinstance(nombreObjeto, nombreClase)`

## Obtener los metodos de la clase padre:

      class Super:
          def __init__(self, nombre):
              self.nombre = nombre

          def __str__(self):
              return "Mi nombre es " + self.nombre + "."

      class Sub(Super):
          def __init__(self, nombre):
              Super.__init__(self, nombre) # Se utiliza el nombre de la clase a heredar para obtener su constructor

      obj = Sub("Andy")

      print(obj)