# Clase Individuo
class Individuo:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

# Clase CuentaFinanciera
class CuentaFinanciera:
    def __init__(self, propietario, saldo, numero_de_cuenta):
        self.propietario = propietario
        self.saldo = saldo
        self.numero_de_cuenta = numero_de_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Saldo actual: {self.saldo}")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

# Clase Cuadrilátero
class Cuadrilatero:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Clase Disco
class Disco:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.radio

# Clase Novela
class Novela:
    def __init__(self, titulo, escritor, genero, año_de_publicacion):
        self.titulo = titulo
        self.escritor = escritor
        self.genero = genero
        self.año_de_publicacion = año_de_publicacion

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_escritor(self):
        return self.escritor

    def establecer_escritor(self, escritor):
        self.escritor = escritor

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def obtener_año_de_publicacion(self):
        return self.año_de_publicacion

    def establecer_año_de_publicacion(self, año):
        self.año_de_publicacion = año

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.escritor}, Género: {self.genero}, Año de Publicación: {self.año_de_publicacion}")

# Clase Melodia
class Melodia:
    def __init__(self, titulo, cantante, disco, duracion):
        self.titulo = titulo
        self.cantante = cantante
        self.disco = disco
        self.duracion = duracion

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_cantante(self):
        return self.cantante

    def establecer_cantante(self, cantante):
        self.cantante = cantante

    def obtener_disco(self):
        return self.disco

    def establecer_disco(self, disco):
        self.disco = disco

    def obtener_duracion(self):
        return self.duracion

    def establecer_duracion(self, duracion):
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo '{self.titulo}' de {self.cantante}...")

# Clase Articulo
class Articulo:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def obtener_cantidad_disponible(self):
        return self.cantidad_disponible

    def establecer_cantidad_disponible(self, cantidad):
        self.cantidad_disponible = cantidad

    def calcular_total(self, cantidad):
        if cantidad > self.cantidad_disponible:
            print("No hay suficiente stock.")
        else:
            return cantidad * self.precio

# Clase Alumno
class Alumno:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def aprobado(self):
        promedio = self.calcular_promedio()
        return promedio >= 6.0

# Ejemplos de uso
individuo = Individuo("Carlos", 30, "Masculino")
individuo.presentarse()

cuenta = CuentaFinanciera(individuo, 1500, "987654321")
cuenta.depositar(700)
cuenta.retirar(300)
cuenta.consultar_saldo()

cuadrilatero = Cuadrilatero(8, 12)
print(f"Área del cuadrilátero: {cuadrilatero.calcular_area()}")
print(f"Perímetro del cuadrilátero: {cuadrilatero.calcular_perimetro()}")

disco = Disco(10)
print(f"Área del disco: {disco.calcular_area()}")
print(f"Circunferencia del disco: {disco.calcular_circunferencia()}")
