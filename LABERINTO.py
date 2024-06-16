def count_paths(maze, start, destination):
    if not maze or maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
        return 0
    
    m, n = len(maze), len(maze[0])
    # Crear una matriz dp de m x n inicializada en 0
    dp = [[0] * n for _ in range(m)]
    
    # Inicializar la posición de inicio si no hay obstáculo
    dp[start[0]][start[1]] = 1
    
    # Llenar la matriz dp de acuerdo a los límites definidos por el punto de destino
    for i in range(start[0], destination[0]+1):
        for j in range(start[1], destination[1]+1):
            if i == start[0] and j == start[1]:
                continue  # Saltar la inicialización del punto de inicio que ya hicimos
            if maze[i][j] == 0:
                if i > start[0]:
                    dp[i][j] += dp[i-1][j]  # Sumar camino desde arriba si no es la primera fila
                if j > start[1]:
                    dp[i][j] += dp[i][j-1]  # Sumar camino desde la izquierda si no es la primera columna
    
    # El número de caminos posibles para llegar al destino definido
    return dp[destination[0]][destination[1]]

# Ejemplo de uso con un punto de inicio y un destino definidos
maze = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
start = (0, 0)  # Punto de inicio (0, 0)
destination = (2, 2)  # Punto de destino (2, 2)

print(f'{count_paths(maze, start, destination)} rutas posibles')
