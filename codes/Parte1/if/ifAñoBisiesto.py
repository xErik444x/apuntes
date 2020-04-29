año = int(input("Introduzca un año:"))

if año <= 1580:
    print("No está dentro del período del calendario gregoriano")
    exit()
if año % 4 != 0:
    print("El año es un año comun.")
elif año % 100 != 0:
     print("El año es un año bisiesto.")
elif año % 400 != 0:
     print("El año es un año comun.")
else:
    print("El año es un año bisiesto.")