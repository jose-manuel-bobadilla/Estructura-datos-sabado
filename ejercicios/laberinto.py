laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba

# Encontrar inicio y salida
for i in range(len(laberinto)):
    for j in range(len(laberinto[0])):
        if laberinto[i][j] == 'S':
            inicio = (i, j)
        elif laberinto[i][j] == 'E':
            salida = (i, j)

def resolver_laberinto(x, y, camino):
    if (x, y) == salida:
        camino.append((x, y))
        return True  # Se encontró la salida

    if not (0 <= x < len(laberinto) and 0 <= y < len(laberinto[0])) or laberinto[x][y] in ('X', '*'):
        return False  # Fuera de los límites o en una pared

    laberinto[x][y] = '*'  # Marcar como visitado
    camino.append((x, y))

    for dx, dy in movimientos:
        if resolver_laberinto(x + dx, y + dy, camino):
            return True  # Si un camino lleva a la salida, terminar

    camino.pop()  # Retroceder si no hay salida
    return False

camino = []
if resolver_laberinto(*inicio, camino):
    print("¡Salida encontrada!")
    print("Camino:", camino)
else:
    print("No hay solución.")
