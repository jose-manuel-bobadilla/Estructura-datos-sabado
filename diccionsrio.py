persona = dict()

def agregar_valor(clave: str, valor : str):
    persona.update({clave : valor})

def eliminar_persona( clave):
    persona.pop(clave)

while True:
    
    decision = int(input("Seleccione 1 para agregar, 2 para eliminar, 3 para mostrar lista, 0 para cerrar: "))

    if decision == 1:
        clave = input("Agregue codigo: ")
        nombre = input("Agregue un nombre: ")
        agregar_valor(clave, nombre)

    elif decision == 2:
         clave = input("Ingrese el código que desea eliminar: ")
         persona.pop(clave) 
         print("Se elimino correctamente")

    elif decision == 3:
        print(persona)

    elif decision == 0:
        break

    

print(persona)




