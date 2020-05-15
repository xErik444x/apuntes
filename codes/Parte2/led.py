
numeros2 = [
["###",
"# #",
"# #",
"# #",
"###"],
["  #",
 "  #",
 "  #",
 "  #",
 "  #"],
["###",
 "  #",
 "###",
 "#  ",
 "###"],
["###",
 "  #",
 "###",
 "  #",
 "###"],
["# #",
 "# #",
 "###",
 "  #",
 "  #"],
["###",
"#  ",
"###",
"  #",
"###",],
["###",
"#  ",
"###",
"# #",
"###",],
["###",
"  #",
"  #",
"  #",
"  #",],
["###",
"# #",
"###",
"# #",
"###",],
["###"
,"# #"
,"###"
,"  #"
,"  #"]]

def generarLed(numero):
    xnumeros = ""
    for x in range(5):
        for z in numero:
                xnumeros +=(numeros2[int(z)][x])
                xnumeros += "   "
        xnumeros += "\n"
    print(xnumeros)

ejecutar = True
print("------------|Numeros a Led|------------")
print("-Para salir presione -1 -")
while ejecutar:
    inNumero = input("Ingresa el numero:") #26 maximo
    if inNumero == "-1":
        ejecutar = False
        exit()
    if inNumero.isdigit():
        if int(inNumero) > 0:
            listaDeNumeros = list(inNumero)
            generarLed(listaDeNumeros)
    else:
        print("el numero ingresado no es valido.")




