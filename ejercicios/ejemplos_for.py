def suma ():
    numero = int(input("numero: "))

    cont = 0 

    for i in range (numero):
    
        cont += 1
        print  (cont)
    
def resta ():
    numero = int(input("numero: "))
    cont = numero
    
    for i in range (numero + 1):
        print (cont)
        cont -= 1
        
def suma_numeros():
    numero = int(input("Ingrese un número: "))  # Pedimos el número
    suma = 0  # Inicializamos la variable acumuladora

    for i in range(1, numero + 1):  # Desde 1 hasta 'numero' (incluido)
        suma += i  # Sumamos cada número a la variable acumuladora

    print(f"La suma de los primeros {numero} números es: {suma}")  # Mostramos el resultado

def tabla ():
    
   val1 = int(input("Ingrese un número: "))
   
   cont = 0
   
   for i in range (10):
       cont += 1
       multi = val1 * cont
       print (f"{val1} * {cont} = {multi}")

def pares_impar():
    pares = []  # Lista para números pares
    impares = []  # Lista para números impares

    N_i = int(input("Ingrese el número inicial: "))
    N_f = int(input("Ingrese el número final: "))

    for i in range(N_i, N_f + 1):  # Recorremos desde N_i hasta N_f (incluido)
        if i % 2 == 0:
            pares.append(i)  # Agregamos a la lista de pares
        else:
            impares.append(i)  # Agregamos a la lista de impares

    print("Números pares:", pares)
    print("Números impares:", impares)

pares_impar()
