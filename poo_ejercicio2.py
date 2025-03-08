class Empleado:
    nombre = str
    edad = int
    salario = 0.0
    
    def __init__(self, nombre: str, edad : int, salario : float ):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        
    def trabajar (self):
        return f"El trabajador {self.nombre} esta ocupado"
    
    def recibir_pago(self, monto : int):
      self.salario += monto 
      return f"El trabajador {self.nombre} ha recibido un pago de ${monto}. Salario actual: ${self.salario}"

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje : str):
        super().__init__(nombre, edad, salario)
        self.lenguaje = lenguaje
        
    def trabajar (self):
        return f"El trabajador {self.nombre} esta ocupado trabajando en {self.lenguaje}"
    
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, equipoCargo : str):
        super().__init__(nombre, edad, salario)
        self.equipoCargo = equipoCargo
        
    def trabajar (self):
        return f"El trabajador {self.nombre} esta ocupado dirigiendo al equipo de {self.equipoCargo}"
    
# Prueba del código
dev = Desarrollador("Carlos", 25, 2000, "Python")
gerente = Gerente("Laura", 40, 5000, "Diseño")

print(dev.trabajar())  # "El trabajador Carlos está programando en Python."
print(dev.recibir_pago(1500))  # "Carlos ha recibido un pago de $1500..."

print(gerente.trabajar())  # "El trabajador Laura está dirigiendo al equipo de Diseño."
print(gerente.recibir_pago(3000))  # "Laura ha recibido un pago de $3000..."


    
        