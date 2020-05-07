def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise #Retorna el valor del error, en este caso ArithmeticError

try:
    badFun(0) # el raise retorna ArithmeticError
    badFun("a") # el raise retorna TypeError porque no se puede dividir una letra por 0
except ArithmeticError:
    print("¡Ya veo!")
except TypeError:
    print("Error de valor")


print("FIN.")