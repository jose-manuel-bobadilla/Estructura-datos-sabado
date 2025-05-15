import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier

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
        encontrado = False

        while actual:
            if actual.datos["CC"] == cedula:
                encontrado = True
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"🗑️ Paciente con cédula {cedula} eliminado de la lista.")
                break
            anterior = actual
            actual = actual.siguiente

        if not encontrado:
            print(f"❌ Paciente con cédula {cedula} no encontrado.")
        return encontrado

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
                 "Diagnóstico": str(fila["Diagnóstico"]).strip()
             }
             self.agregar_paciente(datos_paciente)
         print("📂 Datos cargados desde el archivo.")
     else:
         print("⚠️ Archivo Excel no encontrado. Se creará uno nuevo al guardar.")


#  Árbol de decisiones  
def crear_y_entrenar_modelo():
    # Datos de entrenamiento ficticios para crear un modelo inicial
    X = [
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],  # Enfermedad Respiratoria Común
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],  # Tuberculosis
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],  # Cáncer de Pulmón
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],  # Enfermedad Respiratoria Común
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],  # Enfermedad Respiratoria Común
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],  # Tuberculosis
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],  # Tuberculosis
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0],  # Enfermedad Respiratoria Común
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],  # Cáncer de Pulmón
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],  # Enfermedad Respiratoria Común
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],  # Tuberculosis
    [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],  # Cáncer de Pulmón
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],  # Cáncer de Pulmón
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],  # Enfermedad Respiratoria Común
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0]   # Tuberculosis
    ]
    y = [ 'Enfermedad Respiratoria Común',  # Paciente con síntomas típicos de enfermedad respiratoria
    'Tuberculosis',  # Paciente con síntomas típicos de tuberculosis
    'Cáncer de Pulmón',  # Paciente con síntomas típicos de cáncer de pulmón
    'Enfermedad Respiratoria Común',
    'Enfermedad Respiratoria Común',
    'Tuberculosis',
    'Tuberculosis',
    'Enfermedad Respiratoria Común',
    'Cáncer de Pulmón',
    'Enfermedad Respiratoria Común',
    'Tuberculosis',
    'Cáncer de Pulmón',
    'Cáncer de Pulmón',
    'Enfermedad Respiratoria Común',
    'Tuberculosis']
    
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X, y)
    
    return clf

#  Función para capturar datos del paciente y hacer diagnóstico 
def capturar_datos(lista, modelo):
    CC = input("Ingrese la cédula del paciente: ").strip()
    
    # Evitar cédulas repetidas
    if lista.buscar_paciente_por_cedula(CC):
        print("⚠️ Ya existe un paciente con esa cédula.")
        return

    nombre = input("Ingrese el nombre del paciente: ").strip()
    edad = input("Ingrese la edad del paciente: ").strip()

    # Captura de síntomas
    tos = int(input("¿Tienes tos persistente o recurrente? (1=Sí, 0=No): "))
    fiebre = int(input("¿Has tenido fiebre recientemente? (1=Sí, 0=No): "))
    dificultad_respirar = int(input("¿Sientes dificultad para respirar o falta de aire al realizar actividades cotidianas? (1=Sí, 0=No): "))
    moco = int(input("¿Has notado un aumento de moco o flema? (1=Sí, 0=No): "))
    dolor_pecho = int(input("¿Sientes dolor o malestar en el pecho al respirar profundamente? (1=Sí, 0=No): "))
    sangre_esputo = int(input("¿Has notado sangre en tu esputo o flema? (1=Sí, 0=No): "))
    sudores_nocturnos = int(input("¿Tienes sudores nocturnos excesivos? (1=Sí, 0=No): "))
    perdida_peso = int(input("¿Has perdido peso sin razón aparente? (1=Sí, 0=No): "))
    fiebre_noche = int(input("¿Tienes fiebre, especialmente por la tarde o noche? (1=Sí, 0=No): "))
    fatiga = int(input("¿Te sientes fatigado o débil con frecuencia? (1=Sí, 0=No): "))
    ronquera = int(input("¿Tienes ronquera o cambios en tu voz? (1=Sí, 0=No): "))

    sintomas = {
        "tos": tos,
        "fiebre": fiebre,
        "dificultad_respirar": dificultad_respirar,
        "moco": moco,
        "dolor_pecho": dolor_pecho,
        "sangre_esputo": sangre_esputo,
        "sudores_nocturnos": sudores_nocturnos,
        "perdida_peso": perdida_peso,
        "fiebre_noche": fiebre_noche,
        "fatiga": fatiga,
        "ronquera": ronquera
    }

    # Usar el modelo entrenado para hacer un diagnóstico
    X_nuevo = [[sintomas['tos'], sintomas['fiebre'], sintomas['dificultad_respirar'], sintomas['moco'], sintomas['dolor_pecho'],
                sintomas['sangre_esputo'], sintomas['sudores_nocturnos'], sintomas['perdida_peso'], sintomas['fiebre_noche'],
                sintomas['fatiga'], sintomas['ronquera']]]

    diagnostico = modelo.predict(X_nuevo)[0]

    datos_paciente = {
        "CC": CC,
        "Nombre": nombre,
        "Edad": edad,
        "Diagnóstico": diagnostico
    }

    lista.agregar_paciente(datos_paciente)

#  Menú Principal 
def menu():
    ruta_excel = "/workspaces/Estructura-datos-sabado/proyecto final/Prueba2.xlsx"
    lista = Lista_enlazada_pacientes()
    lista.cargar_desde_excel(ruta_excel)

    # Crear y entrenar el modelo de árbol de decisiones solo una vez
    modelo = crear_y_entrenar_modelo()

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
            capturar_datos(lista, modelo)

        elif opcion == "2":
            lista.mostrar_lista()

        elif opcion == "3":
            cedula = input("Ingrese la cédula a buscar: ").strip()
            lista.buscar_paciente_por_cedula(cedula)

        elif opcion == "4":
            lista.mostrar_lista()
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

#  Iniciar programa 
menu()
