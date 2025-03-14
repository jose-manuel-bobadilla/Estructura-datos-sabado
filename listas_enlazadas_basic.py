from typing import Optional

class Node:
    
    def __init__(self, numero: int)->None:
        self.dato = numero
        self.next : Optional["Node"] = None
        
class ListaEnlazada:
    
    def __init__(self):
        self.cabeza : Optional[Node] = None
        
    def agregar(self, numero:int)->None:
        nodo = Node(numero)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo
        

# Gettters
def get_nombre(self) -> str:
        return self.nombre  # Devuelve el nombre

def get_edad(self) -> int:
        return self.edad  # Devuelve la edad
    
#setters 

def set_nombre(self, nuevo_nombre: str) -> None:
        self.nombre = nuevo_nombre  # Cambia el nombre
        
def set_edad(self, nueva_edad: int) -> None:
        if nueva_edad > 0:  # Validación opcional
            self.edad = nueva_edad
            
# esta funcion sirve para confirmar si algun elemento esta repetido   

def existe (self, animal: Animal)-> bool:
        
        nodo_actual = self.cabeza
        
        while nodo_actual is not None:
            if (nodo_actual.dato.get_nombre() == animal.get_nombre() and 
        nodo_actual.dato.get_tipoAnimal() == animal.get_tipoAnimal()):
                return True
            
        nodo_actual = nodo_actual.next 
        return False
    
#esta funcion sirve para agregar

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

        
    
        