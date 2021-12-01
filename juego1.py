pisos = [1, 2, 3]
bajar = [1, 2]
subir = [2, 3]

accion = ["bajar", "BAJAR", "subir", "SUBIR"]

#piso_actual = input("¿donde estas? ")

def piso(x):

    
    if x in pisos:
        if x in subir:
            input("¿a que piso quieres bajar? ")
            
          
        if x in bajar:
            input("¿a que piso quieres subir? ")
            
        if x in bajar and x in subir:
            input ("¿quieres bajar o subir? ")
            

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

print(piso(3))

