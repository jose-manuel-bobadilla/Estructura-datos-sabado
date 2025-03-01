def potencia (base,exponente):
    if exponente == 0:
     return 1       
    return base*potencia(base,exponente - 1)
    base = 4
    exponente = 5     
    resultado = potencia(base,exponente)

    print (resultado)
        
def sumar_digitos(n):
    n = 123
    
    if n < 10:
        return n
    
    return (n % 10) + sumar_digitos(n // 10)

def invertir_numero(n):
    if n < 10:
        return str(n)
    
    return str(n % 10) + invertir_numero(n// 10)

def contar_digito(n, d):
    if n == 0:  # Caso base: cuando el número se vuelve 0
        return 0
    
    ultimo_digito = n % 10  # Extraemos el último dígito
    if ultimo_digito == d:
        return 1 + contar_digito(n // 10, d)  # Sumamos 1 si es igual a d
    else:
        return contar_digito(n // 10, d)  # Llamamos a la función sin sumar

def sumar_n (n):
    if n == 1:
     return 1
 
    return n + sumar_n(n-1) 

  
n = 2
result = sumar_n(n)
print(result)