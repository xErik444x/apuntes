def misplit(strng):
    array = []
    palabra = ""
    for x in range(len(strng)):
        if strng[x] == " " :
            array.append(palabra)
            palabra = ""
        else:
            palabra += strng[x]
    return(array)

print(len(misplit("Ser o no ser, esa es la pregunta")))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
print(("Ser o no ser, esa es la pregunta").split(" "))