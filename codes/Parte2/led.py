
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
                xnumeros += " "
        xnumeros += "\n"
    print(xnumeros)

inNumero = input("Ingresa el numero:")
listaDeNumeros = list(inNumero)

generarLed(listaDeNumeros)




