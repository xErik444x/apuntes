palabra = input("Ingresa la palabra u oracion: ").upper().replace(" ", "")

cant_letras = len(palabra)
cadena_al_reves =""
while cant_letras > 0:
    cant_letras -= 1
    cadena_al_reves += palabra[cant_letras]

print("palabra:", palabra)
print("cadena_al_reves:", cadena_al_reves)
if (cadena_al_reves == palabra):
    print("Es palindrome.")
else:
    print("NO es palindrome.")