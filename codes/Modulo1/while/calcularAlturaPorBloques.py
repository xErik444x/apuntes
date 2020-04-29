bloques = int(input("Ingrese el número de bloques:"))
altura = 0
bloquesPuestos = 1
while bloques >0:
    altura +=1
    bloquesPuestos += 1
    bloques -= bloquesPuestos 

print("La altura de la pirámide:", altura)
