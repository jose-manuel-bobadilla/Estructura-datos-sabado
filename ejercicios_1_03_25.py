class Vehiculo:
    
    marca : str
    color: str
    modelo: int
    cilindraje: int 
    n_ruedas: int
    combustible = int
    tipo = str 
    
    def __init__(self, marca:str, combustible: int, tipo: str, )->None:
        self.marca = marca
        self.combustible = combustible 
        self.tipo = tipo  
        
    def __str__(self)-> str :
        return f"La marca del vehiculo es {self.marca}, es un/a {self.tipo} y el nivel del combustible es de {self.combustible}%"
    
    def encender(self):
         
        if self.combustible <= 10:
            print("El nivel del combustible es bajo, ir a gasolineria")
        elif self.combustible:
                print ("tiene gasolina")
    
    def acelerar(self):
        while self.combustible > 10:
            self.combustible -= 10
            print(f"Ahora el combustible es de {self.combustible}%")
        if self.combustible <= 10:
            print("El combustible es bajo")
            
                
                
                
        
    


class Moto(Vehiculo):
    pass

class Carro (Vehiculo):
    pass

  
  
Vehiculo1 = Vehiculo("mazda", 40 , "carro")
print(Vehiculo1)
Vehiculo1.encender()
Vehiculo1.acelerar()


moto1 = Moto("Susuki", 20, "moto")
print(moto1)
moto1.encender()


carro1 = Carro("Renault", 10, "carro")
print (carro1)
carro1.encender()
