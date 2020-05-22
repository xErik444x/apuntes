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
> Se pueden utilizar mas clases como super, con mas parametros. `class hijo(padre,madre)`

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

+ Tambien se puede utilizar la función `super()`:

      class Super:
        def __init__(self, nombre):
            self.nombre = nombre

        def __str__(self):
            return "Mi nombre es " + self.nombre + "."

      class Sub(Super):
        def __init__(self, nombre):
            super().__init__(nombre)


+ Probando propiedades: variables de clase

      class Super:
          supVar = 1

      class Sub(Super):
          subVar = 2

      obj = Sub()

      print(obj.subVar)
      print(obj.supVar)

+ Herencias multiples:
        class Nivel1:
            varia1 = 100
            def __init__(self):
                self.var1 = 101

            def fun1(self):
                return 102


        class Nivel2(Nivel1):
            varia2 = 200
            def __init__(self):
                super().__init__()
                self.var2 = 201
            
            def fun2(self):
                return 202


        class Nivel3(Nivel2):
            varia3 = 300
            def __init__(self):
                super().__init__()
                self.var3 = 301

            def fun3(self):
                return 302


        obj = Nivel3()

        print(obj.varia1, obj.var1, obj.fun1())
        print(obj.varia2, obj.var2, obj.fun2())
        print(obj.varia3, obj.var3, obj.fun3())


## Excepciones
> Las excepciones tambien son clases.

    try:
        i = int("Hola!")
    except Exception as e:
        print(e)
        print(e.__str__())


+ Crear una propia excepcion:


      class MyZeroDivisionError(ZeroDivisionError):	
        pass

      def doTheDivision(mine):
        if mine:
          raise MyZeroDivisionError("peores noticias")
        else:		
          raise ZeroDivisionError("malas noticias")

      for mode in [False, True]:
        try:
          doTheDivision(mode)
        except ZeroDivisionError:
          print('División entre cero')


      for mode in [False, True]:
        try:
          doTheDivision(mode)
        except MyZeroDivisionError:
          print('Mi división entre cero')
        except ZeroDivisionError:
          print('División entre cero original')

<br>

          class PizzaError(Exception):
              def __init__(self, pizza, mensaje):
                  Exception.__init__(self, mensaje)
                  self.pizza = pizza


          class DemasiadoQuesoError(PizzaError):
              def __init__(self, pizza, queso, mensaje):
                  PizzaError.__init__(self, pizza, mensaje)
                  self.queso = queso


          def makePizza(pizza, queso):
            if pizza not in ['margherita', 'capricciosa', 'calzone']:
              raise PizzaError(pizza, "no hay tal pizza en el menú")
            if queso > 100:
              raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
            print("¡Pizza lista!")


          for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
            try:
              makePizza(pz, ch)
            except DemasiadoQuesoError as tmce:
              print(tmce, ':', tmce.queso)
            except PizzaError as pe:
              print(pe, ':', pe.pizza)

## Iterador
+ ``__iter__()`` el cual debe devolver el objeto en sí y que se invoca una vez (es necesario para que Python inicie con éxito la iteración).
+  ``__next__()`` el cual debe devolver el siguiente valor (primero, segundo, etc.) de la serie deseada: será invocado por las sentencias for/in para pasar a la siguiente iteración; si no hay más valores a proporcionar, el método deberá lanzar la excepción StopIteration.


        class Fib:
          def __init__(self, nn):
            print("__init__")
            self.__n = nn
            self.__i = 0
            self.__p1 = self.__p2 = 1

          def __iter__(self):
            print("__iter__")		
            return self

          def __next__(self):
            print("__next__")				
            self.__i += 1
            if self.__i > self.__n:
              raise StopIteration
            if self.__i in [1, 2]:
              return 1
            ret = self.__p1 + self.__p2
            self.__p1, self.__p2 = self.__p2, ret
            return ret

        for i in Fib(10):
          print(i)

+ El objeto iterador se instancia primero.
+ Después, Python invoca el método ``__iter__`` para acceder al iterador real.
+ El método ``__next__`` se invoca once veces: las primeras diez veces produce valores útiles, mientras que la ultima finaliza la iteración.


## La sentencia yield

> Se puede ver a la palabra clave reservada yield como un hermano más inteligente de la sentencia return, con una diferencia esencial.

Ejemplo:

    def fun(n):
        for i in range(n):
            return i
+ El ``for`` no podria terminar porque terminaria en el primer return.

      def fun(n):
          for i in range(n):
              yield i

      for v in fun(5):
        print(v)
+ Con el ``yield``, se sigue ejecutando y retornando valores.


## Cómo construir tu propio generador

> ¿Qué pasa si necesitas un generador para producir las primeras n potencias de 2 ?
> Los generadores pueden usarse en `listas de compresion`:

            def potenciasDe2(n):
                potencia = 1
                for i in range(n):
                    yield potencia
                    potencia *= 2

            t = [x for x in potenciasDe2(5)]

            print(t)

> Tambien funciona de manera normal:

          def potenciasDe2(n):
              potencia = 1
              for i in range(n):
                  yield potencia
                  potencia *= 2

          for v in potenciasDe2(8):
              print(v)

+ Compresion de listas:

      lst = []

      for x in range(10):
          lst.append(1 if x % 2 == 0 else 0)

      print(lst)
<br>

          lst = [1 if x % 2 == 0 else 0 for x in range(10)]

          print(lst)
  
## La función lambda

> Una función lambda es una función sin nombre (también puedes llamarla una función anónima).

``lambda parámetros: expresión``

>  Tal cláusula ``devuelve el valor de la expresión al tomar en cuenta el valor del argumento lambda ``actual.
---
Ejemplo:

      dos = lambda : 2
      cuadrado = lambda x : x * x
      potencia = lambda x, y : x ** y

      for a in range(-2, 3):
          print(cuadrado(a), end=" ")
          print(potencia(a, dos()))

Vamos a analizarlo:

+ La primer lambda es una función sin parametros que siempre devuelve un 2. 
+ La segunda es una función anónima de un parámetro que devuelve el valor de su argumento al cuadrado.
+ La tercer lambda toma dos parametros y devuelve el valor del primero elevado al segundo.
---