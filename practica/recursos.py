class Recurso:
    def __init__(self, nombre, capacidad_total, unidad):
        self.nombre = nombre
        self.capacidad_total = capacidad_total
        self.unidad = unidad
        self.disponible = capacidad_total  # Definir la cantidad disponible
        self.uso = 0

    def asignar(self, cantidad):
        if cantidad <= self.disponible:
            self.disponible -= cantidad
            self.actualizar_uso()
            return True
        else:
            return False
        
    def liberar(self, cantidad):
        self.disponible += cantidad
        self.actualizar_uso()

    def actualizar_uso(self):
        self.uso = ((self.capacidad_total - self.disponible) / self.capacidad_total) * 100

    def __str__(self):
        return f"Nombre: {self.nombre}, Capacidad Total: {self.capacidad_total} {self.unidad}, Disponible: {self.disponible} {self.unidad}, Uso: {self.uso:.2f}%"

class Cpu(Recurso):
    def __init__(self, capacidad_total= 100):
        super().__init__("CPU", capacidad_total, "%")

class Ram(Recurso):
    def __init__(self, capacidad_total):
        super().__init__("RAM", capacidad_total, "GB")
    
class Disco(Recurso):
    def __init__(self, capacidad_total):
        super().__init__("Disco Duro", capacidad_total, "GB")

class Proceso():
    def __init__(self, nombre, requiere_cpu = 0, requiere_ram = 0, requiere_disco = 0):
        self.nombre = nombre
        self.estado = "Listo"
        self.requiere_cpu = requiere_cpu
        self.requiere_ram = requiere_ram
        self.requiere_disco = requiere_disco
        self.recursos_asignados = {
            "cpu": 0,
            "ram": 0,
            "disco": 0
        }
        

    def __str__(self):
     return (f"proceso: {self.nombre} ({self.estado})\n"
             f"Requiere:\n"
             f"CPU: {self.requiere_cpu}%\n"
             f"RAM: {self.requiere_ram} GB\n"
             f"Disco: {self.requiere_disco} GB\n"
             f"Recursos Asignados:\n"
             f"CPU: {self.recursos_asignados['cpu']}%\n"
             f"RAM: {self.recursos_asignados['ram']} GB\n"
             f"Disco: {self.recursos_asignados['disco']} GB\n")

class SistemaOperativo():
    def __init__(self):
        self.recursos = {
            "cpu": Cpu(),
            "ram": Ram(2048),
            "disco": Disco(500)
        }

    def agregar_proceso(self, nombre, requiere_cpu, requiere_ram, requiere_disco):
       proceso = Proceso(self, nombre, requiere_cpu, requiere_ram, requiere_disco)
       return "Aqui se crean recursos "
    
    def asignar_recursos(self, proceso):
        print ("Aqui se asignan los procesos")

    def mostrar_recursos(self):
        print("Recursos del sistema:")
        
    def mostrar_procesos(self):
        print("Aqui se muestran los procesos en uso:")

    def finalizar_proceso(self, proceso):
        print("Aqui se finalizan los procesos")
       

# Bloque principal (debe estar fuera de la clase)

if __name__ == "__main__":
    memoria = Recurso("Memoria RAM", 16, "GB")
    print(memoria)
    memoria.asignar(5)
    print(memoria)
    print("Liberando 2 GB ")
    memoria.liberar(2)
    print(memoria)

    cpu = Cpu()
    print(cpu)

    ram = Ram(2048)
    print(ram)

    disco = Disco(500)
    print(disco)

    cpu.asignar(20)
    ram.asignar(512)
    disco.asignar(1)

    print("----------------------------------------")
    print(cpu)
    print(ram)
    print(disco)