from colorama import Fore,init
from funciones.calcular import *
salir = False
while salir != True:
    init()
    print(Fore.MAGENTA + """
    -------------Calculadora re loca--------------
    Seleccione la opción a realizar:
    """,Fore.YELLOW+'1',Fore.MAGENTA,""".Sumar
    """,Fore.YELLOW+'2',Fore.MAGENTA,""".Restar
    """,Fore.YELLOW+'3',Fore.MAGENTA,""".Multiplicar
    """,Fore.YELLOW+'4',Fore.MAGENTA,""".Dividir
    """,Fore.YELLOW+'0',Fore.MAGENTA,""".Salir
    """,Fore.YELLOW+'9',Fore.MAGENTA,""".Limpiar
    ----------------------------------------------
    """, sep="")
    opcion = int(input("Ingrese la opción:"))
    if opcion == 0:
        salir = True
        print("Finalizado con exito.")
    if opcion == 1:
        print(Fore.YELLOW, sumar())
        input("")
    elif opcion == 2:
        print(Fore.YELLOW,restar())
        input("")
    elif opcion == 3:
        print(Fore.YELLOW,multiplicar())
        input("")
    elif opcion == 4:
        print(Fore.YELLOW,dividir())
        input("")
    elif opcion == 9:
        limpiar()
    else:
        print("Opción equivocada.")
