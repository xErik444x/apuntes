"""
---------------Encuentra la palabra--------------
|                                               |
| Escribe palabras hasta encontrar la contraseña|
|                                               |
-------------------------------------------------
"""
p = input("Ingresa la palabra:")

while True:
    if p == "chupacabras":
        break
    else:
        p = input("Esa no es, volve a intentar:")
        
print("Saliste del ciclo")