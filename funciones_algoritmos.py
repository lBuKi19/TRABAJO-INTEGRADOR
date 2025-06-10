import time  # Para medir tiempos de ejecución
from formateo_visualizacion import *

# ALGORITMOS DE ORDENAMIENTO

def bubble_sort(peliculas, input):
    """Ordena películas segun categoría seleccionada usando Bubble Sort"""
    pelis_copia = peliculas.copy()  # Trabajar sobre una copia
    n = len(pelis_copia)
    inicio = time.time()  # Iniciar cronómetro
    
    # Algoritmo Bubble Sort
    for i in range(n):
        for j in range(0, n-i-1):
            if pelis_copia[j][input] < pelis_copia[j+1][input]:  # Orden descendente
                pelis_copia[j], pelis_copia[j+1] = pelis_copia[j+1], pelis_copia[j]
    
    # Mostrar tiempo de ejecución
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    # Resultados
    print(f"\n🔄 Películas ordenadas por {input} (Bubble Sort - Descendente):")
    return pelis_copia 

def quick_sort(peliculas, input, reverse=False):
    """Ordena películas según categoría seleccionada usando Quick Sort"""

    def quicksort(arr):
        """Función recursiva de Quick Sort"""
        if len(arr) <= 1:  # Caso base
            return arr
        
        pivot = arr[len(arr) // 2][input]  # Pivote del medio
        right = [x for x in arr if x[input] > pivot]    # Mayores que pivote
        middle = [x for x in arr if x[input] == pivot] # Iguales al pivote
        left = [x for x in arr if x[input] < pivot]   # Menores que pivote
        
        #condicional que determina orden ascendente o descendente
        if reverse:
            return quicksort(left) + middle + quicksort(right)
        else:
            return quicksort(right) + middle + quicksort(left)  # Combinar resultados
    
    inicio = time.time()
    pelis_ordenadas = quicksort(peliculas.copy())
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    print(f"⚡ Películas ordenadas por {input} (Quick Sort):")
    return pelis_ordenadas

# ALGORITMOS DE BÚSQUEDA 

def busqueda_lineal(peliculas, input, opcion):
    """Busca películas por título/genero usando búsqueda lineal"""
    encontradas = []
    columna = opcion
    if opcion == 'titulo':
        print(f"🔍 Buscando películas con '{input}' en el título...")    
    elif opcion == 'genero':
        print(f"🔍 Buscando películas de genero '{input}'...")
    elif opcion == 'año':
        print(f"🔍 Buscando películas por año '{input}'...")

    inicio = time.time()
    
    # Búsqueda lineal - revisar cada elemento
    for pelicula in peliculas:
        if opcion == 'año':
            if input == pelicula[columna]:
                encontradas.append(pelicula)
        else:
            if input in pelicula[columna].lower():
                encontradas.append(pelicula)
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    if encontradas:
        print(f"🔍 Se encontraron {len(encontradas)} resultados")
        return encontradas
    else:
        print(f"❌ No se encontraron películas o series con esas características")


def busqueda_binaria(peliculas, input_categoria, eleccion):
    """Busca segun categoria seleccionada usando búsqueda binaria"""
    
    print(f"📅 Buscando películas/series usando búsqueda binaria...")
    inicio = time.time()
    
    # Primero ordenar usando funcion ya definida (requisito para búsqueda binaria)
    pelis_ordenadas = quick_sort(peliculas, input_categoria, reverse=True)
    encontradas = []
    low, high = 0, len(pelis_ordenadas) - 1
    # Algoritmo de búsqueda binaria
    while low <= high:
        mid = (low + high) // 2  # Punto medio
        
        if pelis_ordenadas[mid][input_categoria] == eleccion:
            # Encontramos una coincidencia
            encontradas.append(pelis_ordenadas[mid])
            
            # Buscar coincidencias adyacentes (mismo año)
            i = mid - 1
            while i >= 0 and pelis_ordenadas[i][input_categoria] == eleccion:
                encontradas.append(pelis_ordenadas[i])
                i -= 1
            
            i = mid + 1
            while i < len(pelis_ordenadas) and pelis_ordenadas[i][input_categoria] == eleccion:
                encontradas.append(pelis_ordenadas[i])
                i += 1
            break
            
        elif pelis_ordenadas[mid][input_categoria] < eleccion:
            low = mid + 1  # Buscar en mitad superior
        else:
            high = mid - 1  # Buscar en mitad inferior
    
    tiempo = time.time() - inicio
    print(f"⏱️  Tiempo de ejecución: {tiempo:.6f} segundos")
    
    if encontradas:
        print(f"Se encontraron {len(encontradas)} películas/series:")
        return encontradas
    else:
        print(f"No se encontraron películas/series")

#ALGORITMO DE RECOMENDACIÓN
def algo_recomendaciones(peliculas, input_generos):
    pelis_ordenadas = quick_sort(peliculas, input='rating')
    generos = input_generos.split()
    #armar lista de recomendaciones
    recomendaciones = []
     # buscar coincidencias de genero 2 o 3 si es posible
    coincidencias = 0
    for peli in pelis_ordenadas:
        for genero in generos:
            if genero in peli['genero'].lower():
                coincidencias +=1
        if coincidencias >= len(generos)-1:
            recomendaciones.append(peli)
        coincidencias = 0

    return recomendaciones
    
