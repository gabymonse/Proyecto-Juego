primarios = ["amarillo", "azul", "rojo", "AMARILLO", "AZUL", "ROJO"]
primario = ["Amarillo", "Azul", "Rojo"]


class Colores():
    def __init__(self):
        self.color1 = 0
        self.color2 = 0
        self.morado = ["rojo", "azul", "ROJO", "AZUL"]
        self.naranja = ["amarillo", "rojo", "AMARILLO", "ROJO"]
        self.verde = ["amarillo", "azul", "AMARILLO", "AZUL"]

    def color(self):
        print("¡Creemos colores secundarios!")
        print("los colores primarios son:")
        print(primario)
        print("escoge 2 de los 3 colores primarios:")
        self.color1 = input("Color 1: ")
        self.color2 = input("Color 2: ")
        self.secundario()

    def secundario(self):
        if self.color1 in self.morado and self.color2 in self.morado:
            print("rojo y azul crean Morado")
        if self.color1 in self.naranja and self.color2 in self.naranja:
            print("rojo y amarillo crean Naranja")
        if self.color1 in self.verde and self.color2 in self.verde:
            print("azul y amarillo crean Verde")


colors = Colores()
colors.color()


        