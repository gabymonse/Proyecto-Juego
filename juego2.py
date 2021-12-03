pisos = [1, 2, 3]
bajar = [1, 2]
subir = [2, 3]
accion = ["bajar", "BAJAR", "subir", "SUBIR"]

class Ascensor():

    def __init__(self):
        self.x = 0
        self.s = 0
        self.b = 0
        self.sb = 0

    def piso(self,x, s,b,sb):
        self.x = x
        self.s = s
        self.b = b
        self.sb = sb
        
        if self.x in pisos:
            if self.x in subir:
                self.s
            if self.x in bajar:
                self.b
            if self.x in subir and self.x in bajar:
                self.sb

uno= input("en que pisos estas? ")
dos = input("¿a que piso quieres bajar?  ")
tres = input("¿a que piso quieres subir? ")
cuatro = input("¿quieres bajar o subir?  ")
print(Ascensor.piso( uno, dos, tres, cuatro))  