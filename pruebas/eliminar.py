import pandas as pd
import os

# Ruta del archivo
archivo = "usuarios.xlsx"

# Verificar si el archivo existe
if os.path.exists(archivo):
    # Leer los datos
    datos = pd.read_excel(archivo)

    # Mostrar los datos actuales
    print("Datos actuales:")
    print(datos)

    # Pedir al usuario qué quiere eliminar (por nombre o ID)
    criterio = input("\n¿Deseas eliminar por nombre o por ID? (escribe 'nombre' o 'id'): ").strip().lower()

    if criterio == "nombre":
        valor = input("Escribe el nombre exacto que deseas eliminar: ").strip()
        datos_filtrados = datos[datos["Nombre"] != valor]

    elif criterio == "id":
        valor = input("Escribe el ID exacto que deseas eliminar: ").strip()
        datos_filtrados = datos[datos["ID"].astype(str) != valor]

    else:
        print("Criterio no válido. Usa 'nombre' o 'id'.")
        exit()

    # Guardar el archivo actualizado
    datos_filtrados.to_excel(archivo, index=False)
    print("\nRegistro eliminado (si existía). Archivo actualizado.")

    # Mostrar los datos después de eliminar
    print("\nDatos actuales:")
    print(datos_filtrados)

else:
    print("El archivo no existe. No hay datos para eliminar.")
