# def l100kmtompg(litros):
#     galones = litros / 3.785411784
#     millas = 100 * 1000 / 1609.344
#     return millas / galones
    
# def mpgtol100km(millas):
#     km100 = millas * 1609.344 / 1000 / 100
#     litros = 3.785411784
#     return litros / km100


# print(l100kmtompg(3.9))
# print(l100kmtompg(7.5))
# print(l100kmtompg(10.))
# print(mpgtol100km(60.3))
# print(mpgtol100km(31.4))
# print(mpgtol100km(23.5))

grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,) # {'Erik': (10, 7, 4)}
    else:
        grupo[nombre] = (calif,)

print(grupo)