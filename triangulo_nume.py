def triangulo():
    numero = int(input("Escriba la cantidad de números que tiene el triángulo: "))
    
    for i in range(1, numero + 1):  
        for j in range(1, i + 1):  
            print(j, end=",") 
        print()  

triangulo()  
