# Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
# Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
# Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que ingrese el valor nuevamente.
# Si el valor de entrada es válido, será regresado como resultado.

def readint(prompt, min, max):
    assert prompt > min
    assert prompt < max
    return prompt

Ejecutar = True

while Ejecutar:
    try:
        v = readint(int(input("Ingresa un numero de -10 a 10: ")), -10, 10)
        print("El numero es:", v)
        Ejecutar = False
    except ValueError:
        print("Error, Entrada incorrecta.")
    except AssertionError:
        print("Error, el valor no está en el rango permitido, min=-10 , max=10")

