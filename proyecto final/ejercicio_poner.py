import pandas as pd
import os

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
        print("✅ Paciente agregado a la lista.")

    def mostrar_lista(self):
        lista_datos = []
        actual = self.cabeza
        while actual:
            lista_datos.append(actual.datos)
            actual = actual.siguiente

        if lista_datos:
            df = pd.DataFrame(lista_datos)
            print("\n📋 Lista de pacientes:")
            print(df)
        else:
            print("📭 No hay pacientes registrados.")

    def buscar_paciente_por_cedula(self, cedula):
        actual = self.cabeza
        while actual:
            if actual.datos["CC"] == cedula:
                print("✅ Paciente encontrado:")
                print(pd.DataFrame([actual.datos]))
                return actual.datos
            actual = actual.siguiente
        print("❌ Paciente no encontrado.")
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
                print(f"🗑️ Paciente con cédula {cedula} eliminado.")
                return True
            anterior = actual
            actual = actual.siguiente
        print(f"❌ Paciente con cédula {cedula} no encontrado.")
        return False

    def convertir_a_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.datos)
            actual = actual.siguiente
        return lista

    def guardar_en_excel(self, ruta_archivo):
        df = pd.DataFrame(self.convertir_a_lista())
        df.to_excel(ruta_archivo, index=False)
        print("💾 Datos guardados en Excel.")

    def cargar_desde_excel(self, ruta_archivo):
        if os.path.exists(ruta_archivo):
            df = pd.read_excel(ruta_archivo)
            for _, fila in df.iterrows():
                datos_paciente = {
                    "CC": str(fila["CC"]).strip(),
                    "Nombre": str(fila["Nombre"]).strip(),
                    "Edad": str(fila["Edad"]).strip(),
                    "Síntomas": str(fila["Síntomas"]).strip()
                }
                self.agregar_paciente(datos_paciente)
            print("📂 Datos cargados desde el archivo.")
        else:
            print("⚠️ Archivo Excel no encontrado. Se creará uno nuevo al guardar.")

# === Función para capturar paciente desde consola ===
def capturar_datos(lista):
    CC = input("Ingrese la cédula del paciente: ").strip()
    
    # Evitar cédulas repetidas
    if lista.buscar_paciente_por_cedula(CC):
        print("⚠️ Ya existe un paciente con esa cédula.")
        return

    nombre = input("Ingrese el nombre del paciente: ").strip()
    edad = input("Ingrese la edad del paciente: ").strip()
    sintomas = input("Ingrese los síntomas del paciente: ").strip()

    datos_paciente = {
        "CC": CC,
        "Nombre": nombre,
        "Edad": edad,
        "Síntomas": sintomas
    }

    lista.agregar_paciente(datos_paciente)

# === Menú Principal ===
def menu():
    ruta_excel = "/workspaces/Estructura-datos-sabado/proyecto final/Prueba2.xlsx"
    lista = Lista_enlazada_pacientes()
    lista.cargar_desde_excel(ruta_excel)

    while True:
        print("""
=== MENÚ DE OPCIONES ===
1. Agregar paciente
2. Mostrar pacientes
3. Buscar paciente por cédula
4. Eliminar paciente por cédula
5. Guardar pacientes en Excel
6. Salir
        """)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            capturar_datos(lista)

        elif opcion == "2":
            lista.mostrar_lista()

        elif opcion == "3":
            cedula = input("Ingrese la cédula a buscar: ").strip()
            lista.buscar_paciente_por_cedula(cedula)

        elif opcion == "4":
            cedula = input("Ingrese la cédula del paciente a eliminar: ").strip()
            eliminado = lista.eliminar_paciente_por_cedula(cedula)
            if eliminado:
                lista.guardar_en_excel(ruta_excel)

        elif opcion == "5":
            lista.guardar_en_excel(ruta_excel)

        elif opcion == "6":
            print("👋 Programa finalizado.")
            break

        else:
            print("❗ Opción no válida. Intente de nuevo.")

# === Iniciar programa ===
menu()




