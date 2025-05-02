import pandas as pd

# Clase de los hospitales
class Hospital:
    def __init__(self, nombre: str, nit: int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio

    def __str__(self):
        return f"NIT: {self.nit}, Organización: {self.nombre}, Sede: {self.sede}, Municipio: {self.municipio}"

# Nodo del BST
class Nodo:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital
        self.izquierda = None
        self.derecha = None

#  Arbol de Búsqueda de hospitales
class ArbolHospitales:
    def __init__(self):
        self.raiz = None

    def insertar(self, hospital):
        if self.raiz is None:
            self.raiz = Nodo(hospital)
        else:
            self._insertar_recursivo(self.raiz, hospital)

    def _insertar_recursivo(self, nodo_actual, hospital):
        if hospital.nit < nodo_actual.hospital.nit:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(hospital)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, hospital)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(hospital)
            else:
                self._insertar_recursivo(nodo_actual.derecha, hospital)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.hospital)
            self.inorden(nodo.derecha)

    def buscar_hospital(self, nodo, nit_buscado):
        if nodo is None:
            return None
        if nodo.hospital.nit == nit_buscado:
            return nodo.hospital
        elif nit_buscado < nodo.hospital.nit:
            return self.buscar_hospital(nodo.izquierda, nit_buscado)
        else:
            return self.buscar_hospital(nodo.derecha, nit_buscado)

# 📥 Carga y limpieza de datos
hospitales = pd.read_csv("/workspaces/Estructura-datos-sabado/excel2/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426.csv")

hospitales.rename(columns={
    'Razón Social Organización': 'nombre',
    'Número NIT': 'nit',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio'
}, inplace=True)

hospitales['nit'] = hospitales['nit'].str.replace(',', '')
hospitales['nit'] = hospitales['nit'].astype(int)

#  Crear el árbol e insertar hospitales
arbol = ArbolHospitales()

for index, row in hospitales.iterrows():
    hospital = Hospital(
        nombre=row['nombre'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    arbol.insertar(hospital)

#  Mostrar hospitales ordenados por NIT
print("🏥 Hospitales ordenados por NIT (Recorrido in-order):")
arbol.inorden(arbol.raiz)

#  Buscar un hospital por NIT
print("\n Búsqueda de hospital por NIT:")
nit_buscado = int(input("Ingrese el NIT del hospital a buscar: "))
resultado = arbol.buscar_hospital(arbol.raiz, nit_buscado)

if resultado:
    print("\n Hospital encontrado:")
    print(resultado)
else:
    print("\n Hospital no encontrado.")

    
