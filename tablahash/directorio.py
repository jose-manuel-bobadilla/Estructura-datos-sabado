class Persona:
    def __init__(self, nombre: str, telefono: int, dire: str):
        self.nombre = nombre
        self.telefono = telefono
        self.dire = dire 

    def cal_hash(self):
        return hash((self.nombre, self.telefono)) 

class TablaHash:
    
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]  

    def cal_posicion(self, telefono):
        return hash(telefono) % self.tamaño

    def agregar(self, nombre, telefono, dire):  
        posicion = self.cal_posicion(telefono)
        self.tabla[posicion].append((nombre, telefono, dire))  
        print(f"Agregada en {posicion}: {nombre}, {telefono}, {dire}")

    def buscar(self):
        
      new_n = input("Ingrese el nombre: ")
      new_t = int(input("Ingrese el número telefónico: "))

      for lista in self.tabla:
        for nombre, telefono, dire in lista:
            if new_n == nombre and new_t == telefono:
                return f"Encontrado: {nombre}, {telefono}, {dire}"
    
      return "No encontrado o datos incorrectos."

if __name__ == "__main__":
    tabla = TablaHash()
    tabla.agregar("Juan", 123456, "Calle 1")
    tabla.agregar("Maria", 654321, "Calle 2")
    tabla.agregar("Pedro", 1, "Calle 3")
    
    print(tabla.buscar())