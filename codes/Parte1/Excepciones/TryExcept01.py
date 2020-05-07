try:
    primerNumero = int(input("Ingresa el primer numero: "))
    segundoNumero = int(input("Ingresa el segundo numero: "))
    
    if segundoNumero != 0:
        print(primerNumero / segundoNumero)
    else:
        print("Esta operacion no puede ser realizada.")
    
    print("FIN.")
except:
    print("Error al ingresar un numero.")