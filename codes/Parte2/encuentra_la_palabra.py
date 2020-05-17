palabra1 = input("Ingresa el texto: ".upper().replace(" ", ""))
palabra2 = input("Ingresa la palabra a buscar: ".upper().replace(" ", ""))

encontrado = False
for char in palabra2:
    if palabra1.find(char) >-1:
        encontrado = True
        continue
    else:
        encontrado = False
        print("No se encontró")
        break
if encontrado == True:
    print("Se encontró")