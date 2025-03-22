def verificar_balance(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}
    
    for i, simbolo in enumerate(expresion):
        if simbolo in '({[':
            pila.append((simbolo, i))  # Guardamos símbolo y posición
        elif simbolo in ')}]':
            if not pila or pila[-1][0] != pares[simbolo]:
                return f"Expresión: {expresion}\nError en posición {i}: '{simbolo}' no tiene apertura válida"
            pila.pop()  # Eliminar el último símbolo abierto válido
    
    if pila:
        simbolo, posicion = pila[-1]
        return f"Expresión: {expresion}\nError en posición {posicion}: '{simbolo}' no tiene cierre válido"
    
    return f"Expresión: {expresion}\n✅ La expresión está correctamente balanceada"

# Ejemplo de uso con dos expresiones
expresion_correcta = "{[()]}()"  
expresion_incorrecta = "{[(])}"  

print(verificar_balance(expresion_correcta))  
print("\n" + "-" * 40 + "\n")  # Separador visual
print(verificar_balance(expresion_incorrecta))  


