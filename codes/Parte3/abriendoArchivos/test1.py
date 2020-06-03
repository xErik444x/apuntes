import sys
try:
    stream = open("C:\\Users\\Erik\\Desktop\\apuntes\\codes\\Parte3\\abriendoArchivos\\texto.txt","rt", encoding='utf-8')
    print(stream.read())
    stream.close()
except Exception as ex:
    print("Error al abrir el archivo:", ex)
