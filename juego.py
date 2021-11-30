#-----PISOS------------
pisos = [1, 2, 3]
piso_1 = pisos[0]
piso_2 = pisos[1]
piso_3 = pisos[2]

#----CLASE USUARIO---------

class Usuario():
   
    def __init__(self, piso):
        self.piso = piso

    def __repr__(self):
        return self.piso


    def donde_estoy(self,piso):
        piso =input("en que piso estas? ") 
        
        if piso in pisos:
            return piso
        else:
            return "piso 1, 2 o 3"
      

#----CLASE ELEVADOR----------

class Ascensor(Usuario):
    def __init__(self, piso):
        super().__init__(piso)

    def donde_voy(self, bajar_o_subir):
        self.bajar_o_subir = bajar_o_subir
        acciones = ["bajar", "subir", "BAJAR", "SUBIR"]
        voy = input("quiero...")
        pisos = [1, 2, 3]
        if voy in acciones:
            donde = input("a que piso? ")
            if donde in pisos:
                return


#----LLAMANDO A LAS CLASES----

persona = Usuario.donde_estoy(pisos, pisos)
print(persona)




#ascensor va subiendo print subiendo. if ascensor va bajando print bajando



