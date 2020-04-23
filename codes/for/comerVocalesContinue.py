userWord = input("ingresa una palabra:")
userWord = userWord.upper() #pasa a mayus
for letra in userWord: #crea un bucle a partir de la palabra
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    if letra == "U":
        continue
    else:
        print(letra)