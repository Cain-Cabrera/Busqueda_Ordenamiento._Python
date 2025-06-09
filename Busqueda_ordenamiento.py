import random
import time
########### ALGORITMOS DE BUSQUEDA ###########

legajos = random.sample(range(1000,1000000), 100)

def busqueda_binaria(lista,objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1 

    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
        return medio
    
    elif lista[medio] < objetivo:

        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:

        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

########### ALGORITMOS DE ORDENAMIENTO ###########

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# MOSTRAR LEGAJO ORIGINAL
print("Legajos original:", legajos)

# TIEMPO BUBBLESORT
inicio_orden = time.time()
bubble_sort(legajos)
fin_orden = time.time()
print("Legajos ordenados:", legajos)
print(f"Tiempo de bubble_sort: {fin_orden - inicio_orden:.6f} segundos")

# LEGAJO AL AZAR
objetivo = random.choice(legajos)
print(f"Buscando el legajo: {objetivo}")

# MOSTRAR LEGAJO ORIGINAL
inicio_lineal = time.time()
resultado_lineal = busqueda_lineal(legajos, objetivo)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Búsqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo_lineal:.6f} segundos")

# MOSTRAR TIME BUSQUEDA BINARIA
inicio_binaria = time.time()
resultado_binaria = busqueda_binaria(legajos, objetivo)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria
print(f"Búsqueda Binaria: Resultado = {resultado_binaria}, Tiempo = {tiempo_binaria:.6f} segundos")
