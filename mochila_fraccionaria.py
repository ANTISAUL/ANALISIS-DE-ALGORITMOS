def mochila_fraccionaria(capacidad, pesos, valores):
    items = [(i, valores[i], pesos[i], valores[i] / pesos[i]) for i in range(len(valores))]
    items.sort(key=lambda x: x[3], reverse=True)
    
    valor_total = 0
    peso_total = 0
    for item in items:
        if capacidad <= 0:
            break
        indice, valor, peso, razon = item
        cantidad_a_tomar = min(peso, capacidad)
        valor_total += cantidad_a_tomar * razon
        peso_total += cantidad_a_tomar
        capacidad -= cantidad_a_tomar
    
    peso_sobrante = capacidad
    return valor_total, peso_sobrante

# Opciones de conjuntos de ítems
opciones = {
    1: {'pesos': [10, 20, 30], 'valores': [60, 100, 120], 'capacidad': 50},
    2: {'pesos': [5, 10, 15], 'valores': [20, 50, 30], 'capacidad': 20},
    3: {'pesos': [25, 35, 45], 'valores': [85, 95, 105], 'capacidad': 60}
}

# Solicitar al usuario que elija una opción
print("Elige una opción de los conjuntos de ítems:")
print("1: Pesos [20, 30, 40], Valores [80, 120, 150], Capacidad 80")
print("2: Pesos [5, 10, 15], Valores [20, 50, 30], Capacidad 20")
print("3: Pesos [25, 35, 45], Valores [85, 95, 105], Capacidad 60")
opcion = int(input("Introduce el número de opción (1, 2, 3): "))

# Asegurarse de que la opción sea válida
if opcion in opciones:
    pesos = opciones[opcion]['pesos']
    valores = opciones[opcion]['valores']
    capacidad = opciones[opcion]['capacidad']
    valor_maximo, peso_sobrante = mochila_fraccionaria(capacidad, pesos, valores)
    print(f"El valor máximo que se puede llevar es: {valor_maximo}")
    print(f"Peso sobrante en la mochila: {peso_sobrante}")
else:
    print("Opción no válida.")
