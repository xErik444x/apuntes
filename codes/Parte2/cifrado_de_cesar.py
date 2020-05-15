x = False
while x == False:
    print("""
    --------------------------------
    Seleccione la opcion a realizar:
    -1: Cifrar Texto
    -2: Descifrar Texto
    -3: Salir
    --------------------------------
    """)
    y = input()
    if y.isdigit() == False:
        print("Solo puedes ingresar numeros.")
        pass
    if y == '1':
        # Cifrado César
        text = input("Ingresa tu mensaje: ")
        cifrado = ''
        for char in text:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) + 1
            if code > ord('Z'):
                code = ord('A')
            cifrado += chr(code)
        print("Cifrado: ", cifrado)
        input()
    if y == '2':
        # Cifrado César
        text = input("Ingresa tu mensaje Cifrado: ")
        cifrado = ''
        for char in text:
            if not char.isalpha():
                continue
            char = char.upper()
            code = ord(char) - 1
            if code > ord('Z'):
                code = ord('A')
            cifrado += chr(code)
        print("Descifrado: ", cifrado)
        input()
    if y == '3':
        x = True
