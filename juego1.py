pisos = [1, 2, 3]
bajar = [1, 2]
subir = [2, 3]

accion = ["bajar", "BAJAR", "subir", "SUBIR"]

#piso_actual = input("¿donde estas? ")

class Ascensor():
    def __init__(self,x):
        self.x = x

    def piso(self,x):
        

        if self.x in pisos:
           if self.x in subir:
              self.s=  input("¿a que piso quieres bajar? ")
           
          
           if self.x in bajar:
              self.b = input("¿a que piso quieres subir? ")
            
           if self.x in bajar and x in subir:
              self.sb=input ("¿quieres bajar o subir? ")
            

    def final(self):
        
        if self.x in subir:
             print("bajando...")
             print("piso ", self.s)
        if self.x in  bajar:
             print("subiendo...")
             print("piso ", self.b)
        if self.x in bajar and self.x in subir:
             print(" aja ", self.sb)
            
    
    #f x in alto:
       # return "bajando..."
    #if x in bajo:

    

      #if bajar_o_subir in accion:
       #  a_donde = input("¿a que piso quieres ir? ")
       #  if a_donde== pisos[0]:
         #     return "solo puedes subir a ", subir
        # if a_donde == pisos[1]:
           #   return "puedes subir a ", pisos[2], " o bajar a ", pisos[0]
         #if a_donde == pisos[2]:
          #     return "puedes bajar a ", bajar

#print(Ascensor.piso(3))
print(Ascensor.final(3))

