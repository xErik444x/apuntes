palabra1 = sorted(input("Ingresa la primera palabra: ").upper().replace(" ", ""))
palabra2 =  sorted(input("Ingresa la segunda palabra: ").upper().replace(" ", ""))
# frase – fresa
if(palabra1 == palabra2):
    print("Son anagramas.")
else:
    print("No son anagramas.")