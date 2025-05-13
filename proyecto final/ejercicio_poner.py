import pandas as pd

# Definir la clase para manejar la lista de pacientes
class ListaPacientes:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print("✅ Paciente agregado a la lista.")

    def mostrar_pacientes(self):
        if self.pacientes:
            print("\n📋 Lista de pacientes:")
            for paciente in self.pacientes:
                print(f"{paciente['Cédula']} {paciente['Nombre']} {paciente['Edad']} {paciente['Diagnóstico']}")
        else:
            print("No hay pacientes registrados.")

    def buscar_paciente(self, cedula):
        paciente = next((p for p in self.pacientes if p["Cédula"] == cedula), None)
        if paciente:
            print(f"\n📝 Información del paciente: {paciente}")
        else:
            print("Paciente no encontrado.")

    def eliminar_paciente(self, cedula):
        paciente = next((p for p in self.pacientes if p["Cédula"] == cedula), None)
        if paciente:
            self.pacientes.remove(paciente)
            print("✅ Paciente eliminado de la lista.")
        else:
            print("Paciente no encontrado.")

    def guardar_en_excel(self, ruta_excel):
        df = pd.DataFrame(self.pacientes)
        df.to_excel(ruta_excel, index=False)
        print("💾 Datos guardados en Excel.")

    def cargar_desde_excel(self, ruta_excel):
        try:
            df = pd.read_excel(ruta_excel)
            # Verificar los encabezados y limpiar si es necesario
            print(f"Encabezados del archivo: {df.columns}")
            df.columns = [col.strip() for col in df.columns]  # Elimina espacios extra en los nombres de las columnas

            if 'Síntomas' in df.columns:
                for _, fila in df.iterrows():
                    paciente = {
                        "Cédula": fila["Cédula"],
                        "Nombre": fila["Nombre"],
                        "Edad": fila["Edad"],
                        "Diagnóstico": fila["Diagnóstico"],
                        "Síntomas": str(fila["Síntomas"]).strip()
                    }
                    self.pacientes.append(paciente)
                print("📥 Datos cargados desde Excel.")
            else:
                print("La columna 'Síntomas' no se encuentra en el archivo. Verifica el archivo Excel.")
        except Exception as e:
            print(f"Error al cargar desde Excel: {e}")

# Función para capturar los síntomas y hacer el diagnóstico
def diagnostico_arbol_decisiones(sintomas):
    # Aquí iría el código de tu árbol de decisiones, por ejemplo:
    # X = ... (ejemplos de síntomas)
    # y = ... (resultados de diagnóstico)
    # clf.fit(X, y)
    # Predicción usando el modelo entrenado
    return "Cáncer de Pulmón"  # Como ejemplo

def capturar_datos(lista):
    print("\n🩺 Ingresando datos del paciente...")
    cedula = input("Número de cédula: ")
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad del paciente: "))
    
    sintomas = []
    sintomas.append(int(input("¿Tienes tos persistente o recurrente? (1=Sí, 0=No): ")))
    sintomas.append(int(input("¿Has tenido fiebre recientemente? (1=Sí, 0=No): ")))
    sintomas.append(int(input("¿Sientes dificultad para respirar o falta de aire al realizar actividades cotidianas? (1=Sí, 0=No): ")))
    sintomas.append(int(input("¿Has notado un aumento de moco o flema? (1=Sí, 0=No): ")))
    sintomas.append(int(input("¿Sientes dolor o malestar en el pecho al respirar profundamente? (1=Sí, 0=No): ")))
    
    diagnostico = diagnostico_arbol_decisiones(sintomas)

    paciente = {
        "Cédula": cedula,
        "Nombre": nombre,
        "Edad": edad,
        "Diagnóstico": diagnostico,
        "Síntomas": sintomas
    }

    lista.agregar_paciente(paciente)

def menu():
    lista = ListaPacientes()
    ruta_excel = '/workspaces/Estructura-datos-sabado/proyecto final/Prueba2.xlsx'

    # Intentar cargar los datos desde Excel
    lista.cargar_desde_excel(ruta_excel)
    
    while True:
        print("\n=== MENÚ DE OPCIONES ===")
        print("1. Agregar paciente")
        print("2. Mostrar pacientes")
        print("3. Buscar paciente por cédula")
        print("4. Eliminar paciente por cédula")
        print("5. Guardar pacientes en Excel")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            capturar_datos(lista)
        elif opcion == "2":
            lista.mostrar_pacientes()
        elif opcion == "3":
            cedula = input("Ingrese la cédula del paciente a buscar: ")
            lista.buscar_paciente(cedula)
        elif opcion == "4":
            cedula = input("Ingrese la cédula del paciente a eliminar: ")
            lista.eliminar_paciente(cedula)
        elif opcion == "5":
            lista.guardar_en_excel(ruta_excel)
        elif opcion == "6":
            print("👋 Programa finalizado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()



