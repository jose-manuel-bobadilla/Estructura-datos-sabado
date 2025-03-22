def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

  
#numero = int(input("Ingrese un número: "))
#print(fibonacci(numero))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" , ")
        a, b = b, a + b

n = int(input("Ingrese el número de términos de la serie Fibonacci: "))
fibonacci(n)
