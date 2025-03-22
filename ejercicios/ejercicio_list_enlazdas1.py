from typing import Optional
class Animal:
    def __init__(self, nombre: str, edad : int, tipoAnimal : str):
        self.nombre = nombre
        self.edad = edad
        self.tipoAnimal = tipoAnimal
        
    def get_nombre(self)-> str:
        return self.nombre
    
    def get_edad(self) -> int:
        return self.edad 
    
    def get_tipoAnimal(self) -> str:
        return self.tipoAnimal
    
    def set_nombre(self, nuevo_nombre: str) -> None:
        self.nombre = nuevo_nombre
        
    def set_edad(self, nueva_edad: int) -> None:
         if nueva_edad > 0:  
            self.edad = nueva_edad
        
class Node:
    
    def __init__(self, animal: Animal)-> None:
        self.dato = animal
        self.next : Optional["Node"] = None
        
class ListaEnlazada:
    def __init__(self):
         self.cabeza : Optional[Node] = None
         
    def agregar(self, animal: Animal) -> bool:  
        if self.existe(animal):
            print(f"El animal {animal.get_nombre()} ({animal.get_tipoAnimal()}) ya está en la lista.")
            return False

        nodo = Node(animal)
        if self.cabeza is None:
            self.cabeza = nodo
            return True  # ✅ Ahora siempre retorna `True` cuando se agrega

        nodo_actual = self.cabeza
        while nodo_actual.next is not None:
            nodo_actual = nodo_actual.next
        nodo_actual.next = nodo
        return True  # ✅ Retorno consistente

        
     # esta funcion sirve para confirmar si algun elemento esta repetido   
    def existe(self, animal: Animal) -> bool:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if (nodo_actual.dato.get_nombre() == animal.get_nombre() and 
                nodo_actual.dato.get_tipoAnimal() == animal.get_tipoAnimal()):
                return True
            nodo_actual = nodo_actual.next  # ✅ Moverse al siguiente nodo dentro del while
        return False

    def mostrar_iterativo(self) -> None:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
             print(f"Nombre: {nodo_actual.dato.get_nombre()}, Tipo: {nodo_actual.dato.get_tipoAnimal()}, Edad: {nodo_actual.dato.get_edad()}")
             nodo_actual = nodo_actual.next

    def mostrar_recursivo(self, nodo_actual=None) -> None:
        if nodo_actual is None:
            nodo_actual = self.cabeza  # Iniciar desde la cabeza
            if nodo_actual is None:  # ✅ Caso base si la lista está vacía
                return
        
        print(f"Nombre: {nodo_actual.dato.get_nombre()}, Tipo: {nodo_actual.dato.get_tipoAnimal()}, Edad: {nodo_actual.dato.get_edad()}")
        
        if nodo_actual.next is not None:  # ✅ Evita llamar con `None`
            self.mostrar_recursivo(nodo_actual.next)  # Llamada recursiva
        

# Crear la lista enlazada
lista_animales = ListaEnlazada()

# Crear algunos animales
perro = Animal("Firulais", 5, "Perro")
gato = Animal("Misu", 3, "Gato")
loro = Animal("Piolín", 2, "Loro")

# Agregar los animales a la lista
print(lista_animales.agregar(perro))  # True (debería agregarse)
print(lista_animales.agregar(gato))   # True (debería agregarse)
print(lista_animales.agregar(loro))   # True (debería agregarse)
print(lista_animales.agregar(perro))  # False (ya existe)

# Mostrar los animales de forma iterativa
print("\nAnimales (iterativo):")
lista_animales.mostrar_iterativo()

# Mostrar los animales de forma recursiva
print("\nAnimales (recursivo):")
lista_animales.mostrar_recursivo()
