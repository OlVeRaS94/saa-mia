from collections import deque

# Estat inicial i final del puzzle
inicio = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

final = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

# Moviments possibles del '0'
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Troba la posició del '0'
def encontrar_espacio(estado):
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                return i, j

# Moure el '0'
def mover(estado, direccion):
    nuevo = [fila[:] for fila in estado]  # Copia l'estat
    x, y = encontrar_espacio(estado)
    dx, dy = direccion
    nx, ny = x + dx, y + dy

    # Comprova si el moviment és vàlid
    if 0 <= nx < 3 and 0 <= ny < 3:
        nuevo[x][y], nuevo[nx][ny] = nuevo[nx][ny], nuevo[x][y]
        return nuevo
    return None  # Si no és vàlid

# Funció principal per trobar la solució
def bfs():
    cola = deque([(inicio, [])])  # Cola amb l'estat inicial i el camí
    visitados = set()  # Conjunt per rastrejar estats visitats

    while cola:
        estado, camino = cola.popleft()  # Extreu l'element frontal

        # Si trobem la solució, retorna el camí
        if estado == final:
            return camino

        # Si ja hem visitat aquest estat, el ignorem
        if tuple(map(tuple, estado)) in visitados:
            continue

        visitados.add(tuple(map(tuple, estado)))  # Marca l'estat com visitat

        # Prova tots els moviments
        for direccion in movimientos:
            nuevo = mover(estado, direccion)
            if nuevo:  # Si el moviment és vàlid
                cola.append((nuevo, camino + [nuevo]))  # Afegeix el nou estat a la cola

    return None  # Si no hi ha solució

# Imprimir l'estat del puzzle
def mostrar(estado):
    for fila in estado:
        print("|", end=" ")
        for valor in fila:
            print(valor if valor != 0 else " ", end=" | ")
        print()
    print()

# Executar la cerca
solucion = bfs()

# Mostrar els resultats
if solucion:
    print("¡Solució trobada!")
    print(f"Passos: {len(solucion)}")

    # Mostrar cada pas
    for i, paso in enumerate(solucion, 1):
        print(f"Pas {i}:")
        mostrar(paso)

    # Mostrar l'estat final
    print("¡Solució final!")
    mostrar(final)
else:
    print("No s'ha trobat solució.")
