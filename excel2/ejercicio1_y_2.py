class Nodo:
    def __init__(self,dato):
        
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:

    def __init__(self):
        self.raiz = None

    def agregar_valor(self, valor):  # Este busca si hay una raiz si no, sigue con agregar_recursivamente
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivamente(self.raiz, valor)

    def _insertar_recursivamente(self, nodo_actual, valor):  
        if valor < nodo_actual.dato:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivamente(nodo_actual.izquierda, valor)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivamente(nodo_actual.derecha, valor)
        
    def preorden(self,nodo): #Mira la raiz luego imprime de izquierda a derecha
        if nodo is not None:
         print (nodo.dato)
         self.preorden(nodo.izquierda)
         self.preorden(nodo.derecha)

    def imprimir_niveles(self):
        if self.raiz is None:
            print("El árbol está vacío")
            return
        
        lista_nodos = [self.raiz]  # Empezamos con la raíz

        while lista_nodos:
            nodo_actual = lista_nodos.pop(0)  # Extraemos el primer nodo
            print(nodo_actual.dato, end=" ")  # Imprimimos el dato del nodo
            
            # Agregamos los hijos a la lista
            if nodo_actual.izquierda:
                lista_nodos.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                lista_nodos.append(nodo_actual.derecha)

    def buscar(self,nodo,busqueda):
        if nodo is None:
            return "El nodo no existe", False
        if nodo.dato == busqueda:
            return F"El nodo {nodo.dato} existe", True 
        if busqueda < nodo.dato:
            return self.buscar(nodo.izquierda, busqueda)
        else:  
         return self.buscar(nodo.derecha, busqueda)
    

# Arbol
arbol = Arbol()
valores = [20, 10, 30, 5, 15, 25, 35]
for v in valores:
    arbol.agregar_valor(v)

# Recorrido en preorden
print("Recorrido en preorden:")
arbol.preorden(arbol.raiz)

# Recorrido por niveles
print("\nRecorrido por niveles:")
arbol.imprimir_niveles()

print() #Print estetico

# Prueba de la funcion buscar
prueba = arbol.buscar(arbol.raiz, 15)
print(prueba)  # ("El nodo existe: 15", True)

prueba = arbol.buscar(arbol.raiz, 99)
print(prueba)  # ("El nodo no existe", False)