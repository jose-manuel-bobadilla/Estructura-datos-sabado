import pandas as pd

class Nodo_paciente:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

class Lista_enlazada_pacientes:
    def __init__(self):
        self.cabeza = None

    def agregar_paciente(self, datos_paciente):
        nuevo = Nodo_paciente(datos_paciente)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print("Paciente agregado a la lista.")

    def mostrar_lista(self):
        lista_datos = []
        actual = self.cabeza
        while actual:
            lista_datos.append(actual.datos)
            actual = actual.siguiente

        if lista_datos:
            df = pd.DataFrame(lista_datos)
            print("\nLista de pacientes:")
            print(df)
        else:
            print("No hay pacientes registrados.")

    def buscar_paciente_por_cedula(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.datos["CC"] == cedula:
                print("Paciente encontrado:")
                print(pd.DataFrame([actual.datos]))
                return actual.datos
            actual = actual.siguiente

        print("Paciente no encontrado.")
        return None

    def eliminar_paciente_por_cedula(self, cedula):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.datos["CC"] == cedula:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Paciente con cédula {cedula} eliminado.")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"Paciente con cédula {cedula} no encontrado.")

    def convertir_a_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.datos)
            actual = actual.siguiente
        return lista

    def paciente(self):
        CC = input("Ingrese la cédula del paciente: ")
        nombre = input("Ingrese el nombre del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        sintomas = input("Ingrese los síntomas del paciente: ")

        datos_paciente = {
            "CC": CC,
            "Nombre": nombre,
            "Edad": edad,
            "Síntomas": sintomas
        }

        self.agregar_paciente(datos_paciente)

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar un nuevo paciente")
    print("2. Mostrar lista de pacientes")
    print("3. Buscar paciente por cédula")
    print("4. Eliminar paciente por cédula")
    print("5. Salir")

def main():
    lista_pacientes = Lista_enlazada_pacientes()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista_pacientes.paciente()
        elif opcion == "2":
            lista_pacientes.mostrar_lista()
        elif opcion == "3":
            cedula = input("Ingrese la cédula del paciente a buscar: ")
            lista_pacientes.buscar_paciente_por_cedula(cedula)
        elif opcion == "4":
            cedula = input("Ingrese la cédula del paciente a eliminar: ")
            lista_pacientes.eliminar_paciente_por_cedula(cedula)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa
main()





