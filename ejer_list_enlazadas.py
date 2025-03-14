from typing import Optional

class Animal:
    def __init__(self, nombre: str, edad: int, TipAnimal: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.TipAnimal = TipAnimal

    # Getters
    def get_nombre(self) -> str:
        return self.nombre

    def get_edad(self) -> int:
        return self.edad

    def get_TipAnimal(self) -> str:
        return self.TipAnimal

class Node:
    def __init__(self, animal: Animal) -> None:
        self.animal = animal  
        self.next: Optional["Node"] = None  

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional[Node] = None

    def agregar(self, nuevo_animal: Animal) -> None:
        if self.existe(nuevo_animal):
            print(f"El animal {nuevo_animal.get_nombre()} ({nuevo_animal.get_TipAnimal()}) ya está en la lista.")
            return

        nuevo_nodo = Node(nuevo_animal)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nuevo_nodo

    def existe(self, animal: Animal) -> bool:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if (nodo_actual.animal.get_nombre() == animal.get_nombre() and 
                nodo_actual.animal.get_TipAnimal() == animal.get_TipAnimal()):
                return True
            nodo_actual = nodo_actual.next
        return False

    # Método iterativo para mostrar todos los animales
    def mostrar_iterativo(self) -> None:
        nodo_actual = self.cabeza
        if nodo_actual is None:
            print("La lista está vacía.")
            return
        
        while nodo_actual is not None:
            animal = nodo_actual.animal
            print(f"Nombre: {animal.get_nombre()}, Edad: {animal.get_edad()}, Tipo: {animal.get_TipAnimal()}")
            nodo_actual = nodo_actual.next

        # Método recursivo para mostrar todos los animales
    def mostrar_recursivo(self, nodo: Optional[Node] = None) -> None:
        if nodo is None:  # Primer llamado
            if self.cabeza is None:
                print("La lista está vacía.")
                return
            nodo = self.cabeza  # Se asigna el primer nodo válido

        # Imprimir el nodo actual
        animal = nodo.animal
        print(f"Nombre: {animal.get_nombre()}, Edad: {animal.get_edad()}, Tipo: {animal.get_TipAnimal()}")

        # Llamada recursiva con el siguiente nodo
        if nodo.next is not None:  # Solo llamamos si hay un siguiente nodo
            self.mostrar_recursivo(nodo.next)

# Ejemplo de uso
lista = ListaEnlazada()
a1 = Animal("Firulais", 5, "Perro")
a2 = Animal("Mishi", 3, "Gato")
a3 = Animal("Luna", 2, "Conejo")

lista.agregar(a1)
lista.agregar(a2)
lista.agregar(a3)

print("\n--- Mostrando Animales (Iterativo) ---")
lista.mostrar_iterativo()

print("\n--- Mostrando Animales (Recursivo) ---")
lista.mostrar_recursivo()