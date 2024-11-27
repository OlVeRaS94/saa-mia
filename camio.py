from collections import deque
import heapq

# Datos de entrada
paquetes = [
    {"peso": 10, "valor": 60},
    {"peso": 20, "valor": 100},
    {"peso": 30, "valor": 120},
    {"peso": 15, "valor": 80},
    {"peso": 25, "valor": 90}
]
capacidad_camion = 50

# Función BFS
def bfs(paquetes, capacidad):
    cola = deque()
    cola.append((0, 0, []))  # valor total, peso total, paquetes seleccionados
    mejor_valor = 0
    mejor_comb = []
    combinaciones_exploradas = 0

    while cola:
        valor_actual, peso_actual, comb_actual = cola.popleft()
        combinaciones_exploradas += 1

        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_comb = comb_actual

        start_index = comb_actual[-1] + 1 if comb_actual else 0
        for i in range(start_index, len(paquetes)):
            paquete = paquetes[i]
            nuevo_peso = peso_actual + paquete["peso"]
            if nuevo_peso <= capacidad:
                nueva_comb = comb_actual + [i]
                nuevo_valor = valor_actual + paquete["valor"]
                cola.append((nuevo_valor, nuevo_peso, nueva_comb))

    return mejor_valor, mejor_comb, combinaciones_exploradas

# Función DFS
def dfs(paquetes, capacidad):
    pila = []
    pila.append((0, 0, []))  # valor total, peso total, paquetes seleccionados
    mejor_valor = 0
    mejor_comb = []
    combinaciones_exploradas = 0

    while pila:
        valor_actual, peso_actual, comb_actual = pila.pop()
        combinaciones_exploradas += 1

        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_comb = comb_actual

        start_index = comb_actual[-1] + 1 if comb_actual else 0
        for i in range(start_index, len(paquetes)):
            paquete = paquetes[i]
            nuevo_peso = peso_actual + paquete["peso"]
            if nuevo_peso <= capacidad:
                nueva_comb = comb_actual + [i]
                nuevo_valor = valor_actual + paquete["valor"]
                pila.append((nuevo_valor, nuevo_peso, nueva_comb))

    return mejor_valor, mejor_comb, combinaciones_exploradas

# Función A*
def a_star(paquetes, capacidad):
    cola = []
    heapq.heappush(cola, (0, 0, 0, []))  # heurística, valor total, peso total, paquetes seleccionados
    mejor_valor = 0
    mejor_comb = []
    combinaciones_exploradas = 0

    while cola:
        heuristica, valor_actual, peso_actual, comb_actual = heapq.heappop(cola)
        combinaciones_exploradas += 1

        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_comb = comb_actual

        start_index = comb_actual[-1] + 1 if comb_actual else 0
        for i in range(start_index, len(paquetes)):
            paquete = paquetes[i]
            nuevo_peso = peso_actual + paquete["peso"]
            if nuevo_peso <= capacidad:
                nueva_comb = comb_actual + [i]
                nuevo_valor = valor_actual + paquete["valor"]
                heuristica = -nuevo_valor / nuevo_peso  # Heurística: valor por unidad de peso
                heapq.heappush(cola, (heuristica, nuevo_valor, nuevo_peso, nueva_comb))

    return mejor_valor, mejor_comb, combinaciones_exploradas

# Ejecutar BFS
mejor_valor_bfs, mejor_comb_bfs, combinaciones_exploradas_bfs = bfs(paquetes, capacidad_camion)
print("BFS - Mejor valor posible:", mejor_valor_bfs)
print("BFS - Paquetes seleccionados:")
for idx in mejor_comb_bfs:
    print(f"  - Paquete {idx+1}: Peso {paquetes[idx]['peso']}, Valor {paquetes[idx]['valor']}")
print("BFS - Combinaciones exploradas:", combinaciones_exploradas_bfs)

# Ejecutar DFS
mejor_valor_dfs, mejor_comb_dfs, combinaciones_exploradas_dfs = dfs(paquetes, capacidad_camion)
print("\nDFS - Mejor valor posible:", mejor_valor_dfs)
print("DFS - Paquetes seleccionados:")
for idx in mejor_comb_dfs:
    print(f"  - Paquete {idx+1}: Peso {paquetes[idx]['peso']}, Valor {paquetes[idx]['valor']}")
print("DFS - Combinaciones exploradas:", combinaciones_exploradas_dfs)

# Ejecutar A*
mejor_valor_a_star, mejor_comb_a_star, combinaciones_exploradas_a_star = a_star(paquetes, capacidad_camion)
print("\nA* - Mejor valor posible:", mejor_valor_a_star)
print("A* - Paquetes seleccionados:")
for idx in mejor_comb_a_star:
    print(f"  - Paquete {idx+1}: Peso {paquetes[idx]['peso']}, Valor {paquetes[idx]['valor']}")
print("A* - Combinaciones exploradas:", combinaciones_exploradas_a_star)

# Comparación de los Resultados
print("\nComparación de los Resultados:")
print(f"BFS - Combinaciones exploradas: {combinaciones_exploradas_bfs}, Mejor valor: {mejor_valor_bfs}")
print(f"DFS - Combinaciones exploradas: {combinaciones_exploradas_dfs}, Mejor valor: {mejor_valor_dfs}")
print(f"A* - Combinaciones exploradas: {combinaciones_exploradas_a_star}, Mejor valor: {mejor_valor_a_star}")
