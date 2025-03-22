def multiplicacion ():

    valor_1 = int(input("Registre el primer valor ")) 
    valor_2 = int(input("Registre el segundo valor ")) 
    
    multi = 0
    
    for i in range(valor_2):
        multi += valor_1
    
    print(f"El resultado de {valor_1} x {valor_2} es: {multi}")
    

def division():
    valor_1 = int(input("Registre el primer valor: ")) 
    valor_2 = int(input("Registre el segundo valor: "))  

    if valor_2 == 0: 
        print("No se puede dividir por cero.")
        return

    divi = 0  

    while valor_1 >= valor_2:  
        valor_1 -= valor_2  
        divi += 1  

    print(f"El resultado de la división entera es: {divi} con residuo {valor_1}")






division()


multiplicacion()
    
    