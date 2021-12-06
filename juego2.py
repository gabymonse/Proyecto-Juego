#pisos = [1, 2, 3]
#bajar = [1, 2]
#subir = [2, 3]
#accion = ["bajar", "BAJAR", "subir", "SUBIR"]

class Ascensor():

    def __init__(self):
        self.x = 0
        self.s = 0
        self.b = 0
        self.sb = 0
        self.pisos = [1, 2, 3]
        self.bajar = [1, 2]
        self.subir = [2, 3]  
        
    def piso(self):
        self.x = input("en que pisos estas? ")
        #self.s = input("¿a que piso quieres bajar?  ")
        #self.b = input("¿a que piso quieres subir? ")
        #self.sb = input("¿quieres bajar o subir?  ")
       
        #print(self.x)
        if self.x in self.pisos:
            if self.x in self.subir:
                self.s = input("¿a que piso quieres bajar?  ")
            if self.x in self.bajar:
                self.b = input("¿a que piso quieres subir? ")
            if self.x in self.subir and self.x in self.bajar:
                self.sb = input("¿quieres bajar o subir?  ")

#uno= input("en que pisos estas? ")
#dos = input("¿a que piso quieres bajar?  ")
#tres = input("¿a que piso quieres subir? ")
#cuatro = input("¿quieres bajar o subir?  ")

elevador = Ascensor()
elevador.piso()