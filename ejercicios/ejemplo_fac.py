numero = 5

def factorial (n)->int :
     res  = 1
    
     for i in range (1, n+1) :
         
        
         res = res * i
         
     return res 
     
#print(factorial(numero))

def facto_while(n: int) -> int:
    res = 1
    contador = 1
    
    while contador <= n:
        res = res * contador
        contador = contador + 1  # Puedes usar contador += 1 también
    
    return res  # Debe estar fuera del while

#numero = int(input("Ingrese un número: "))
#print(facto_while(numero))

def auto_invocacion (n:int)->int:
     if n == 1:
        return n
    
     return auto_invocacion(n-1) * n

print(auto_invocacion(5))