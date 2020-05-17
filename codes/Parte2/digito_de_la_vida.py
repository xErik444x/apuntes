fecha = input("ingrese la fecha en formato AAAA MM DD:").replace(" ","")

while(len(fecha) > 1):
    calcDigito = 0
    for char in fecha:
        calcDigito += int(char)
    fecha = str(calcDigito)

print(fecha)