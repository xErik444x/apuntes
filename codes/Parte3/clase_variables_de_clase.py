class Circulo:

    __pi = 3.1416 # variable de clase, solo le pertenece a la clase, no al objeto /(Circulo.pi)
    def __init__(self,radio):
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * self.__pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(circulo_uno.area())
print(circulo_dos.area())
print(circulo_uno.__dict__) #muestra los atributos y variables del objeto
