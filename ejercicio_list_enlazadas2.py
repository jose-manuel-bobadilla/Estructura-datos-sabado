from typing import Optional
from datetime import datetime  # ✅ Agregar la librería para manejar fechas

class Tarea:
    def __init__(self, descripcion: str, prioridad: int, fechaVencimiento: str) -> None:
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fechaVencimiento = fechaVencimiento

class Node:
    def __init__(self, tarea: Tarea) -> None:  # 🔹 Ahora almacena una instancia de Tarea
        self.tarea = tarea
        self.next: Optional["Node"] = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza: Optional[Node] = None

    def agregar(self, descripcion: str, prioridad: int, fechaVencimiento: str) -> None:
        tarea = Tarea(descripcion, prioridad, fechaVencimiento)  # ✅ Crear una tarea
        nodo = Node(tarea)  # ✅ Crear un nodo con la tarea

        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

    def eliminar_descripcion(self, descripcion: str) -> bool:
        if self.cabeza is None:
            return False  # Lista vacía
    
        # Si la tarea a eliminar está en la cabeza
        if self.cabeza.tarea.descripcion == descripcion:
            self.cabeza = self.cabeza.next
            return True  # Se eliminó la tarea
    
        nodo_actual = self.cabeza
        while nodo_actual.next is not None:
            if nodo_actual.next.tarea.descripcion == descripcion:
                nodo_actual.next = nodo_actual.next.next  # Salta el nodo a eliminar
                return True  # Se eliminó la tarea
            nodo_actual = nodo_actual.next
    
        return False  # Tarea no encontrada

    def mostrar_ordenado(self) -> None:
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        
        tareas = []
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            tareas.append(nodo_actual.tarea)
            nodo_actual = nodo_actual.next
            
        # 🔹 Ordenar por prioridad (descendente) y luego por fecha (ascendente)
        tareas.sort(key=lambda t: (-t.prioridad, datetime.strptime(t.fechaVencimiento, "%Y-%m-%d")))

        print("\n📌 Lista de tareas ordenadas:")
        for tarea in tareas:
            print(f"🔹 {tarea.descripcion} | Prioridad: {tarea.prioridad} | Vence: {tarea.fechaVencimiento}")
            
    def buscar_tarea(self, descripcion: str) -> None:
        nodo_actual = self.cabeza

        while nodo_actual is not None:
            if nodo_actual.tarea.descripcion.lower() == descripcion.lower():  # Ignora mayúsculas/minúsculas
                print("\n🔍 Tarea encontrada:")
                print(f"🔹 Descripción: {nodo_actual.tarea.descripcion}")
                print(f"🔹 Prioridad: {nodo_actual.tarea.prioridad}")
                print(f"🔹 Fecha de vencimiento: {nodo_actual.tarea.fechaVencimiento}")
                return
        
            nodo_actual = nodo_actual.next

        print("\n❌ Tarea no encontrada.")

    def marcar_completada(self, descripcion: str) -> None:
        print("\n----------------------------")
        print(f"Marcando como completada: {descripcion}")
        if self.eliminar_descripcion(descripcion):
            print(f"✅ La tarea '{descripcion}' ha sido eliminada de la lista.")
        else:
            print(f"❌ No se encontró la tarea '{descripcion}' para marcar como completada.")
        print("----------------------------")

# ✅ Prueba del código
lista = ListaEnlazada()
lista.agregar("Hacer la tarea de Python", 2, "2025-03-12")
lista.agregar("Comprar comida", 1, "2025-03-11")

lista.mostrar_ordenado()

lista.marcar_completada("Hacer la tarea de Python")

lista.mostrar_ordenado() 