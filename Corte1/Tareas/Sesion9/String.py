import random

# Crear una matriz 5x10 con valores aleatorios entre 1 y 100
matriz = [[random.randint(1, 100) for _ in range(10)] for _ in range(5)]

# Función para encontrar el número más bajo y su posición
def encontrar_minimo(matriz):
    minimo_valor = min(min(fila) for fila in matriz)
    fila_min, columna_min = next(((fila, columna) for fila, fila_valores in enumerate(matriz) for columna, valor in enumerate(fila_valores) if valor == minimo_valor))
    return minimo_valor, (fila_min, columna_min)

# Función para encontrar el número más alto y su posición
def encontrar_maximo(matriz):
    maximo_valor = max(max(fila) for fila in matriz)
    fila_max, columna_max = next(((fila, columna) for fila, fila_valores in enumerate(matriz) for columna, valor in enumerate(fila_valores) if valor == maximo_valor))
    return maximo_valor, (fila_max, columna_max)

# Función para organizar la matriz en orden descendente
def organizar_matriz(matriz):
    matriz.sort(key=lambda fila: max(fila), reverse=True)

if __name__ == '__main__':
    # Imprimir la matriz original
    print("Matriz Original:")
    for fila in matriz:
        print(fila)
    # Encontrar los números más bajos y más altos junto con sus posiciones
    minimo_valor, pos_minimo = encontrar_minimo(matriz)
    maximo_valor, pos_maximo = encontrar_maximo(matriz)
    print(f"Número más bajo: {minimo_valor} en la posición {pos_minimo}")
    print(f"Número más alto: {maximo_valor} en la posición {pos_maximo}")
    # Organizar la matriz en orden descendente
    organizar_matriz(matriz)
    # Imprimir la matriz organizada
    print("\nMatriz Organizada:")
    for fila in matriz:
        print(fila)
