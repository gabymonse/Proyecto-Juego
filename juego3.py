class Ascensor():
    def __init__(self):
        self.pisos = [1, 2, 3]
        self.bajar = 1
        self.subir = 3
        self.subirbajar = 2  
        self.accion = ["bajar", "BAJAR", "subir", "SUBIR"]
        
    def start(self):
        self.x = int(input("¿en que piso estas? "))
        if self.x in self.pisos:
            self.s()
        
    def s(self):
        if self.x == self.subir:
            self.su= int(input("¿a que piso quieres bajar? "))
            if self.su == 3:
                print("estas en el piso 3")
            if self.su == 1 :
                print("bajando...")
                print("PISO 1 :)")
            if self.su == 2:
                print("bajando...")
                print("PISO 2 :)")
            
        if self.x == self.bajar:
            self.ba = int(input("¿a que piso quieres subir? "))
            if self.ba == 1:
                print("ya estas en el piso 1")
            if self.ba == 2:
                print("subiendo...")
                print("PISO 2 XD")
            if self.ba == 3 :
                print("subiendo...")
                print("PISO 3 XD")
        if self.x == self.subirbajar:
            self.sb()
    
    def sb(self):
        su_ba = input("¿quieres subir o bajar? ")
        if su_ba in self.accion:
            self.y = int(input ("que piso? "))
            if self.y ==2:
                print("ya estas en el piso 2")
            if self.y == 1:
                print("bajando...")
                print("PISO 1 XD")
            if self.y == 3:
                print("subiendo...")
                print("PISO 3 XD")

    #def llamado(self):
        


        


#----
elevador = Ascensor()
elevador.start()




