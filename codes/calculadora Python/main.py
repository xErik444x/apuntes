from funciones.calcular import *
salir = False
while salir != True:
    print("""
    -------------Calculadora re loca--------------
    Seleccione la opción a realizar:
    1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir
    0.Salir
    9.Limpiar
    ----------------------------------------------
    """)
    opcion = int(input("Ingrese la opción:"))
    if opcion == 0:
        salir = True
        print("Finalizado con exito.")
    if opcion == 1:
        print(sumar())
        input("Pulse cualquier tecla para continuar:")
    elif opcion == 2:
        print(restar())
        input("Pulse cualquier tecla para continuar:")
    elif opcion == 3:
        print(multiplicar())
        input("Pulse cualquier tecla para continuar:")
    elif opcion == 4:
        print(dividir())
        input("Pulse cualquier tecla para continuar:")
    elif opcion == 9:
        limpiar()
    else:
        print("Opción equivocada.")
