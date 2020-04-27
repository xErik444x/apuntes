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

> Resumen

+ **and** → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, **(True and True)** es **True**.
+ **or** → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, **(True or False)** es **True**.
+ **not** → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, **not True** es **False**.

---
## Valores lógicos vs. bits individuales

    Los operadores lógicos toman sus argumentos como un todo, independientemente de cuántos bits contengan. Los operadores solo conocen el valor: cero (cuando todos los bits se restablecen) significa False; no cero (cuando se establece al menos un bit) significa True.

## Operadores bitwise
>DATO DE SUMA IMPORTANCIA:

    Los bits se numeran desde cero y el número de bits cero es el más bajo, mientras que el más alto es el número 31.
>Fin del dato de suma importancia.

> opera sobre números binarios a nivel de bits individuales 0 y 1

 * &  (ampersand) - conjunción a nivel de bits.
 * |  (barra vertical) - disyunción a nivel de bits.
 * ~  (tilde) - negación a nivel de bits.
 * ^  (signo de intercalación) - exclusivo a nivel de bits o (xor).

* &  requieres exactamente dos  1  s para proporcionar  1  como resultado.
* |  requiere al menos un  1  para proporcionar  1  como resultado.
* ^  requiere exactamente un  1  para proporcionar  1  como resultado.


> Operaciones bitwise (&, |{representado con I}, y ^)

| Arg A | Arg B | A `&` B | A \| B | A `^` B |
|:---:|:---:|:---:|:---:|:---:|
|0|0|0|0|0|
|0|1|0|1|1|
|1|0|0|1|1|
|1|1|1|1|0|

 >(~)

|Arg A|~A|
|:-:|:-:|
|0|1|
|1|0|

## Operaciones lógicas vs operaciones de bit: continuación
 > Explicación con ejemplos:

    i = 15
    j = 22 
    Si asumimos que los enteros se almacenan con 32 bits, la imagen a nivel de bits de las dos variables será la siguiente:
    i: 00000000000000000000000000001111
    j: 00000000000000000000000000010110 
    ambas variables no son 0, por ende, son True:
     og = i and j 
     # og vale True

    El operador & operará con cada par de bits correspondientes por separado, ej:
    i	 000000000000000000000000000 '01111'
    j	 000000000000000000000000000 '10110' 
    bit = i & j : 000000000000000000000000000  '00110'
    como son la mayoria ceros, el operador & va a actuar y comparar en la ultima parte.
    ej: 0&1 , 1&1,etc, de ahi saca el resultado.

>Negación:

Primero el lógico:
    ``logneg = not i ``, se establece como False.

La negación a nivel de bits es así: `bitneg = ~i `

    i	        0000000000000000000000000000  1111  
    bitneg = ~i 1111111111111111111111111111  0000 

## ¿Para qué puedo usar un operador bitwise?

 >Imagina que eres un desarrollador obligado a escribir una pieza importante de un sistema operativo. Se te ha dicho que puedes usar una variable asignada de la siguiente forma:

    flagRegister = 0x1234
    Cada bit de la variable almacena un valor de si/no.
    uno de todos esos bits te pertenece, esta marcado con una x:
    flagRegister = 000000000000000000000000000000x000
    Si aplicas la operación & a la variable flagRegister vas a tener el siguiente resultado:
    x & 1 = x
    0000000000000000000000000000'1'000 si tu bit se estableció en 1
    0000000000000000000000000000'0'000 si tu bit se reseteo a 0

    Dicha secuencia de ceros y unos, cuya tarea es tomar el valor o cambiar los bits seleccionados, se denomina máscara de bits.
    Construyamos una máscara de bits para detectar el estado de tus bits. Debería apuntar a el tercer bit. Ese bit tiene el peso de 2E3=8. Se podría crear una máscara adecuada mediante la siguiente declaración:
    2E3=8
    theMask = 8

    También puedes hacer una secuencia de instrucciones dependiendo del estado de tu bit i, aquí está:
`if flagRegister & theMask:
    # mi bit está listo
else:
    # mi bit se restablece `

    Reinicia tu bit: asigna un cero al bit, mientras que todos los otros bits deben permanecer sin cambios:
`flagRegister = flagRegister & ~theMask`

`flagregister &= ~theMask `

    Establece tu bit : asigna un 1 a tu bit, mientras que todos los bits restantes deben permanecer sin cambios; usa la siguiente propiedad de disyunción:

`x | 1 = 1`

`x | 0 = x `

    Ya estás listo para configurar su bit con una de las siguientes instrucciones:

`flagRegister = flagRegister | theMask`

`flagRegister |= theMask `

    Niega tu bit: reemplaza un 1 con un 0 y un 0 con un 1
`x ^ 1 = ~x`

`x ^ 0 = x `


    Niega tu bit con las siguientes instrucciones:

`flagRegister = flagRegister ^ theMask`

`flagRegister ^= theMask `


> Resumen operadores bit a bit:

    x = 15, el cual es  0000 1111  en binario.
    y = 16, el cual es  0001 0000  en binario.


+ & hace un bit a bit and (y), por ejemplo, `x & y = 0`, el cual es 0000 0000 en binario.
+ | hace un bit a bit or (o), por ejemplo, `x | y = 31`, el cual es 0001 1111 en binario.
+ ˜ hace un bit a bit not (no), por ejemplo, `˜ x = 240`, el cual es 1111 0000 en binario.
+ ^ hace un bit a bit xor, por ejemplo, `x ^ y = 31`, el cual es 0001 1111 en binario.
+  <>> hace un desplazamiento bit a bit a la derecha, por ejemplo, `y >> 1 = 8`, el cual es 0000 1000 en binario.
+ << hace un desplazamiento bit a bit a la izquierda, por ejemplo,` y << 3 = `, el cual es 1000 0000 en binario.

## Desplazamiento binario
> Python ofrece otra operación relacionada con los bits individuales: shifting

`12345 × 10 = 123450 `
    
    multiplicar por diez es de hecho un desplazamiento de todos los dígitos a la izquierda y llenar el vacío resultante con cero.

`12340 ÷ 10 = 1234 `

    Dividir entre diez no es más que desplazar los dígitos a la derecha.
>
    La computadora realiza el mismo tipo de operación, pero con una diferencia: como dos es la base para los números binarios (no 10)
    Los operadores de cambio en Python son un par de dígrafos: << y >>
`valor << bits`

`valor >> bits`

    var = 17
    varRight = var >> 1
    varLeft = var << 2
    print(var, varLeft, varRight)
    #      17     68       8 

* 17 // 2 → 8 (desplazarse hacia la derecha en un bit equivale a la división de enteros en dos)
* 17 * 4 → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro).

        ejercicio bit a bit
        x = 4 : 0000100
        y = 1 : 0000001
        0010000
        a = x & y : 0000000
        b = x | y : 0000101
        c = ~ x : 1111000
        d = x ^ 5 : 0000101
        e = x >> 2 : 0000001
        f = x << 2 : 0010000

        print(a, b, c, d, e, f) 



---



## Listas / Arrays
>comienza con un corchete abierto y termina con un corchete cerrado
`numeros = [ 10, 5, 7, 2, 1] `

    numeros = [10, 5, 7, 2, 1]
    print("Contenido de la lista:", numeros) # imprimiendo contenido de la lista original.

    print(numeros[0]) # accediendo al primer elemento de la lista. 
    print(numeros) # imprimiendo la lista completa.

### Función len()

> Se usa para ver la longitud de una lista.
 `print("\nLongitud de la lista:", len(numeros))`

### Función del()
>Se usa para eliminar un index y su valor de una lista.
 `del numeros[1]`

### Indices Negativos
>Un elemento con un índice igual a -1 es el último en la lista
`print(numeros[-1])`


## Funciones vs Metodos
>Una función no pertenece a ningún dato: obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado

>Un método es un tipo específico de función,puede cambiar el estado de una entidad seleccionada.

***Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.***


## Agregar items a la lista

* insert `lista.insert(ubicación,valor)` (se puede elegir la posición)
* append `lista.append(valor)` (lo coloca al final de la lista)

## Creando una lista vacia
    miLista = []
    for i in range (5):
    #miLista.append (i + 1) #crea la lista de menor a mayor
    #miLista.insert(0, i + 1) #crea la lista de mayor a menor
    print(miLista)


## Puntos claves de un array

* almacena múltiples objetos
  
+  Las listas pueden estar anidadas, por ejemplo: `miLista = [1, 'a', ["lista", 64, [0, 1], False]]` o `[1, [2, 3], 4]`
  
+ Las listas pueden ser iteradas mediante el uso del bucle 
for:

        miLista = ["blanco", "purpura", "azul", "amarillo", "verde"]
        for color in miLista :
            print(color) 

## Puntos claves de Arrays / Listas
* Metodo sort() para ordenar automaticamente.

        lst = [5, 3, 1, 2, 4]
        print(lst)

        lst.sort ()
        print(lst) # salida: [1, 2, 3, 4, 5]

* Metodo reverse() para invertir una lista

        lst = [5, 3, 1, 2, 4]
        print(lst)
            
        lst.reverse()
        print (lst) # salida: [4, 2, 1, 3, 5]

## Almacenamiento de listas en la memoria.

> Las listas se almacenan de diferentes formas que las variables, por ejemplo, si asignamos una lista a otra lista, ambas listas van a estar en el mismo lugar de memoria, si modificamos una, se modifica la otra y viceversa, ej:

        lista1 = [1]
        lista2 = lista1
        lista1[0] = 2
        lista1.append(3)
        lista2.append("hola")
        print("lista2" , lista2)  #lista2 [2, 3, 'hola']
        print("lista1" , lista1) #lista1 [2, 3, 'hola']

>Si hacemos eso, lo que estamos haciendo es literalmente copiar el nombre de la variable (espacio en memoria) a otra.

## ¿Cómo podemos copiar una lista sin que este ligada a la anterior?

> Esto se puede lograr utilizando un "slice" o "rodaja" asignandole un `:` a la lista nueva, ej:

        lista1 = [1]
        lista2 = lista1[:]
        lista1[0] = 2
        print(lista2)
        #[1]

> Ya no va a estar ligada, por ende, son dos listas diferentes.
 
>Al "slice" o "rodaja" se le puede asignar dos variables, una de inicio y otra de final, ej:  `miLista[inicio:fin-1]`

        # Copiando toda la lista
        lista1 = [1]
        lista2 = lista1[:]
        lista1[0] = 2
        print(lista2) #[1]

        # Copiando parte de la lista
        miLista = [10, 8, 6, 4, 2]
        nuevaLista = miLista[1:3]
        print(nuevaLista) #[8, 6]

## Cosas a tener en cuenta del Slice o Rodaja:

+ Acepta indices negativos en el argumento final.

        miLista = [10, 8, 6, 4, 2]
        nuevaLista = miLista [1:-1]
        print(nuevaLista) # [8, 6, 4]

+ Si pones un argumento que no concuerde a una ubicacion del array al inicio, sin importar el del final, ésta estará vacia, ej:
  
        miLista = [10, 8, 6, 4, 2]
        nuevaLista = miLista [-1:1]
        print(nuevaLista) # []

+ No es necesario poner ambos argumentos, se puede colocar solo uno de los dos, por ejemplo, que inicie en 2 y termine al final: `miLista[2:]`. O tambien ` miLista [:5]` , que comienza en 0 y termina en la posicion 5.


## Instrucción Del con Slice en array

> Cuando usamos la instruccion Del con un slice, logramos que se eliminen x cantidad de elementos y no solo uno, ej:

        miLista = [10, 8, 6, 4, 2]
        del miLista[1:3] 
        print(miLista) # [10, 4, 2]

> Del mismo modo, podemos eliminar todos los elementos:

        miLista = [10, 8, 6, 4, 2]
        del miLista[:] 
        print(miLista) # []

>Si usamos del array, vamos a eliminar la lista PERO NO SU CONTENIDO.

        miLista = [10, 8, 6, 4, 2]
        del miLista 
        print(miLista)

## Comparaciones de listas con IN y NOT IN

>Estos dos comparadores son capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no. Ej:

        elem in miLista #Si está dentro, devuelve True
        elem not in miLista #Si No está dentro, devuelve True

        miLista = [0, 3, 12, 8, 2]

        print(5 in miLista) # False
        print(5 not in miLista) # True
        print(12 in miLista) # True


## comprensión de lista
> una comprensión de lista, la sintaxis especial utilizada por Python para completar o llenar listas masivas. Ej:

        #fila = [PEON_BLANCO for i in range(8)]

        cuadrados = [x ** 2 for x in range(10)]
        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

        cuadrados = [x ** 2 for x in range(10)]
        probabilidades = [x for x in cuadrados if x % 2 != 0] 
        print(probabilidades) #Impares de la lista


## arrays bidimensionales
> Son arrays dentro de otro array o lista. ej: `[[1,2,3],[3,4,5]]`


> Un tablero de ajedrez es un array bidimensional.

    El acceso al campo seleccionado del tablero requiere dos índices: el primero selecciona la fila; el segundo: el número del campo dentro de la fila, el cual es un número de columna.

![Tablero](https://raw.githubusercontent.com/xErik444x/apuntesPython/master/img/tablero.PNG "tablero de ajedrez")

+ Torres en las esquinas:

        tablero[0][0] = TORRE
        tablero[0][7] = TORRE
        tablero[7][0] = TORRE
        tablero[7][7] = TORRE

+ Generando tablero con torres:

        EMPTY = "-"
        TORRE = "TORRE"
        tablero = []

        for i in range(8):
            fila = [EMPTY for i in range(8)]
            tablero.append (fila)

        tablero[0][0] = TORRE
        tablero[0][7] = TORRE
        tablero[7][0] = TORRE
        tablero[7][7] = TORRE

        print(tablero)
---

## Funciones

### ¿De dónde provienen las funciones?

+ De Python mismo: varias funciones (como print()) son una parte integral de Python.
+ De los módulos preinstalados de Python.
+ Directamente del código.
+ Existe una posibilidad más, pero se relaciona con clases, se omitirá por ahora.

> Declaración:

        def tuFuncion ():
            # el cuerpo de la función
> Ej:

        def hola(): 
            print("Hola") 

## Parametros en Funciones

> Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

+ Los parámetros solo existen dentro de las funciones en donde han sido definidos.
+ La asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca.
+ primero se especifican los argumentos posicionales y después los de palabras clave

        def mensaje(nombreCliente, numero):
        print("Ingresa", nombreCliente, "número", numero)

> Paso de argumentos con palabras claves (argumento posicional):
    def presentar (primerNombre, segundoNombre):
        print("Hola, mi nombre es", primerNombre, segundoNombre)

    presentar(primerNombre = "James", segundoNombre = "Bond")
    presentar(segundoNombre = "Skywalker", primerNombre = "Luke")

    # el = se usa para decirle en que variable tiene que ir, aca no importa la posicion.

> Se puede definir los valores desde la propia Funcion:

        def test(a,b = "ya estoy definido"):
            print(a,b) 
        
        test("hola") # hola ya estoy definido
        test("hola","ahora la defino acá")
            # hola ahora la defino acá





## Funcion y Return

> La instrucción `return` devuelve un valor y termina la funcion. Ej:

    def felizAñoNuevo(deseos = True):
        print("Tres ...")
        print("Dos ...")
        print("Uno ...")
        if not deseos:
            return
        print("¡Feliz año nuevo!") 
    
    felizAñoNuevo() # funciona completa
    felizAñoNuevo(False) # llega hasta 'print("uno")'

Otro ejemplo:

    def sumar(a,b):
        return(a+b)
    
    x = int(input("ingrese el primer numero:"))
    z = int(input("ingrese el segundo numero:"))
    
    print(sumar(x,z)) # 4

## NONE

> Se utiliza para asignar un valor nulo a una variable:

    x = None
+ Si una función no devuelve un cierto valor utilizando una cláusula de expresión return, se asume que devuelve implícitamente None

> Retornando un valor None o True dependiendo del argumento:

        def strangeFunction(n):
            if(n % 2 == 0):
                return True
                # si no es par, retorna un valor None
                
        if (strangeFunction(2)): # Si retorna True
            print("hola mundo")

## Listas apartir de funciones:

    def strangeListFunction(n):
        strangeList = []
        for i in range(0, n):
            strangeList.insert(0,n+i)
        return strangeList

    print(strangeListFunction(5)) #[9, 8, 7, 6, 5]






## Las funciones y sus alcances (scopes)
 > Las funciones pueden usar variables definidas anteriormente de ser llamadas
        def miFuncion():
            print("¿Conozco a la variable?", variable)

        variable = 1
        miFuncion() #1



---
## Prioridades

| Prioridad | Operador | tipo|
|:---:|---|---|
|1|!, ~, (tipo), ++, --, +, -| (unario)|
|2|**|
|3|*, /, %|
|4|+, -	|(binario)|
|5|<< >>|
|6|<, <=, >, >=|
|7|==, !=|
|8|&||
|9|l||
|10|&&||
|11|\|\|||
|12|=, +=, -=, *=, /=, %=, &=, ^=, \|=, >>=, <<=\|\| |










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

## Intercambiar variables

+ Con auxiliar:

        variable1 = 1
        variable2 = 2

        auxiliar = variable1
        variable1 = variable2
        variable2 = auxiliar 

+ Sin usar una variable auxiliar:

        variable1 = 1
        variable2 = 2

        variable1, variable2 = variable2, variable1 

* Usando una lista / Array con pocos numeros
    
        miLista = [10, 1, 8, 3, 5]
        miLista [0], miLista [4] = miLista [4], miLista [0]
        miLista [1], miLista [3] = miLista [3], miLista [1]
        #[5, 3, 8, 1, 10]

* Usando un array con muchos numeros
  
        miLista = [10, 1, 8, 3, 5]
        lon = len(miLista)

        for i in range (lon // 2):
            miLista[i], miLista[lon-i-1] = miLista[lon-i-1], miLista[i]
            print(i,lon-i-1)
        print(miLista) 
        #[5, 3, 8, 1, 10]
---

## buscando numero en array o lista

        miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        Encontrar = 5
        Encontrado = False

        for i in range(len(miLista)):
            Encontrado = miLista[i] == Encontrar
            if Encontrado:
                break

        if Encontrado:
            print("Elemento encontrado en el índice", i)
        else:
            print("ausente")


## Usando Slice para encontrar el mayor de una lista.

        miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
        mayor = miLista [0]

        for i in miLista [1:]: 
        # si empezamos desde 1 nos salteamos la comparacion 
        #innecesaria de 17 > 17
        if i > mayor:
                mayor = i

        print(mayor) # 17

        Tambien se pude hacer:
        for i in range(1, len(miLista)):
        if miLista [i]> mayor:
                mayor = miLista[i]

        print(mayor) # 17

## Usando In en array

        sorteados = [5, 11, 9, 42, 3, 49]
        seleccionados = [3, 7, 11, 42, 34, 49]
        aciertos = 0
        numerosAcertados = []
        for numeros in seleccionados:
            if numeros in sorteados: #si el numero esta en la lista
                aciertos += 1
                numerosAcertados.append(numeros)
        print("Aciertos:",aciertos,"Numeros acertados:",numerosAcertados, sep="\n")

## Eliminando repetidos

        miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

        for numero in miLista:
            if numero in miLista:
                del miLista[numero]
        miLista.sort()


        print("La lista solo con elementos únicos:")
        print(miLista)
