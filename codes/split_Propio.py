def misplit(strng):
    array = []
    palabra = ""
    for x in range(len(strng)): # Recorro todo el String
        if strng[x].isspace() : # Si la posicion actual tiene espacio
            if len(palabra) > 0: # Si la palabra formada es mayor que 0
                array.append(palabra) # agregar la palabra al array
                palabra = "" # reiniciar valor de la palabra
        else:
            palabra += strng[x] # Si no tiene espacio, añadir el caracter para formar otra palabra
        if x == len(strng)-1 and len(palabra)> 0:
            array.append(palabra)
    return(array)

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit(" espacio sin espacio con espacio del espacio "))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))