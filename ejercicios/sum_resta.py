def multi():
 resultado = 0 
 n = int(input("Elige el primer numero "))
 n2 = int(input("Elige el segundo numero "))
 for _ in range(n2): 
     resultado +=  n
 print (resultado)
 
 
def dividir(n, n2, contador=0):
    # Caso base: si el dividendo es menor que el divisor, terminamos
    if n < n2:
        return contador, n  # Devolvemos el cociente y el residuo

    # Caso recursivo: restamos el divisor y aumentamos el contador
    return dividir(n - n2, n2, contador + 1)

# Pedir los números solo una vez
n = int(input("Elige el primer número: "))
n2 = int(input("Elige el segundo número: "))

# Llamar la función con los valores ingresados
cociente, residuo = dividir(n, n2)

# Imprimir el resultado
print(f"Resultado: {cociente}, Residuo: {residuo}")



        








            
    
    
dividir()

# multi()