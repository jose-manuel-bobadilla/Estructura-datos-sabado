# # pseudo codigo
# Definir Clase Pila:
#     Definir función __init__():
#         Crear una lista vacía llamada elementos

#     Definir función push(elemento):
#         Agregar elemento a la lista elementos

#     Definir función pop():
#         Si la pila está vacía:
#             Mostrar "Error: La pila está vacía"
#         Si no:
#             Remover y retornar el último elemento de la lista elementos

#     Definir función peek():
#         Si la pila está vacía:
#             Mostrar "Error: La pila está vacía"
#         Si no:
#             Retornar el último elemento de la lista elementos sin removerlo

#     Definir función isEmpty():
#         Si elementos está vacío:
#             Retornar Verdadero
#         Si no:
#             Retornar Falso


#Codigo

class Pila:
    
    def __init__(self):
        self.elementos = []
        
    def push(self, elemento):
        self.elementos.append(elemento)
        
    def pop(self):
        if self.isEmpty():
            print("Error, la lista está vacía")
            return None
        return self.elementos.pop()
    
    def peek(self):
        if self.isEmpty():
            print("Error, la lista está vacía")
            return None
        return self.elementos[-1]
    
    def isEmpty(self):
        return len(self.elementos) == 0

# Pruebas
pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)

print("Elemento en la cima:", pila.peek())  # Debe imprimir 30
print("Elemento eliminado:", pila.pop())  # Debe imprimir 30
print("La pila está vacía?", pila.isEmpty())  # Debe imprimir False
pila.pop()
pila.pop()
print("La pila está vacía?", pila.isEmpty())  # Debe imprimir True

