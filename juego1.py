pisos = [1, 2, 3]
bajar = [pisos[0], pisos[1]]
subir = [pisos[1], pisos[2]]
accion = ["bajar", "BAJAR", "subir", "SUBIR"]

def piso(piso_actual):
 piso_actual = input("¿donde estas? ")
 if piso_actual in pisos:
    bajar_o_subir = input("¿quieres bajar o subir? ")
    if bajar_o_subir in accion:
        a_donde = input("¿a que piso quieres ir? ")
        if a_donde== pisos[0]:
            return "solo puedes subir a ", subir
        if a_donde == pisos[1]:
              return "puedes subir a ", pisos[2], " o bajar a ", pisos[0]
        if a_donde == pisos[2]:
               return "puedes bajar a ", bajar

print(piso(pisos))