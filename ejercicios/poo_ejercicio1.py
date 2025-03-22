class Libro:
    titulo : str
    autor : str
    añoPublicacion : int 
    genero : str
    disponible : True
    
    def __init__(self, titulo:str, autor:str, añoPublicacion:int, genero:str):
        self.titulo = titulo
        self.autor = autor
        self.añoPublicacion = añoPublicacion
        self.genero = genero
        self.disponible = True
        
    def __str__(self)-> str :
        estado = "disponible" if self.disponible else "no disponible"
        return f"El libro titulado {self.titulo}, del autor {self.autor}, esta {estado} "
    
    def prestar(self):
        
        if not self.disponible:
         print ("El libro no esta disponible")
         
        else: 
            self.disponible = False
            print("El  libro fue prestado correctamente")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print("El libro se ha devuelto correctamente")
        else:
            return "El libro ya esta disponible"
            
            
class Revista(Libro):
    def __init__(self, titulo: str, autor: str, añoPublicacion: int, genero: str, edicion: int):
        super().__init__(titulo, autor, añoPublicacion, genero)
        self.edicion = edicion  # Nuevo atributo específico de Revista

    def __str__(self) -> str:
        estado = "disponible" if self.disponible else "no disponible"
        return f"La revista '{self.titulo}', edición {self.edicion}, del autor {self.autor}, está {estado}."
            
        
# Prueba con Libro
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción")
print(libro1)
libro1.prestar()
print(libro1)
libro1.devolver()
print(libro1)

# Prueba con Revista
revista1 = Revista("National Geographic", "Varios", 2024, "Ciencia", 128)
print(revista1)
revista1.prestar()
print(revista1)