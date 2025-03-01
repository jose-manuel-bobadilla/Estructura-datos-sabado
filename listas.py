numeros = []

def agregar(numero:int)-> None :
    numeros.append(numero)
    
def eliminar (numero:int)-> None:
    numeros.pop(numero)
    

    
while True:
    seleccion = int(input('''Seleccione 1 si quiere agregar seleccione 2 si desea eliminar, seleccione 0 para finalizar, 3 mostrar lista: '''))
                          

    if seleccion == 1:
        numero = int(input("Agregue un número a la lista: "))
        agregar(numero)

    elif seleccion == 2:
        numero = int(input("elimine un número de la lista: "))
        eliminar(numero)

    elif seleccion == 0:
        break
    
    elif seleccion == 3:
        print("Lista actual: ")
        print(numeros)
      
print (numeros) 