# Importar módulos necesarios
import sys  # Para funcionalidades del sistema como salir del programa
from formateo_visualizacion import *
from funciones_algoritmos import *

#Función principal que maneja el menú interactivo
def main():
    barra = "="*60
    lista_menu = ["\n1. Cantidad de Resultados por operación", "\nORDENAMIENTO:", "2. Opción lenta, no estoy apurado (Bubble Sort)", "3. Opción rápida, el tiempo es oro! (Quick Sort)", "\nBÚSQUEDA:", "4. Buscar por título (lineal)", "5. Buscar por género (lineal)", "6. Búsqueda por año (lineal)", "7. Búsqueda Binaria ", "8. Recomendación", "9. Salir"]
    # Cargar datos al iniciar
    peliculas = cargar_peliculas()

    print("SISTEMA DE PELÍCULAS y SERIES IMDB")
    
    if peliculas is None:
        sys.exit(1)
    
    # Menú interactivo
    while True:
        print(barra)
        print("MENÚ DE SELCCIÓN")  
        print(barra)    
        # Loop por opciones de menu para mostrar
        for item in lista_menu:
            print(item)
       
        opcion = input("Seleccione una opción (1-9): ").strip()
        
        if opcion == "1":
            limite= input("¿Cuántas resultados deseas mostrar? (10 por defecto): ").strip()
            if limite.isdigit():
                limite = int(limite) 
            else:
                limite = 10
            mostrar_peliculas(peliculas, limite)
        elif opcion == "2":
            input_categoria = input("Ingrese la categoría que desea ordenar (rating, genero, año, título): ").strip().lower()
            mostrar_peliculas(bubble_sort(peliculas, input_categoria))
        elif opcion == "3":
            input_categoria = input("Ingrese la categoría que desea ordenar (rating, genero, año, título): ").strip().lower()
            mostrar_peliculas(quick_sort(peliculas, input_categoria))
        elif opcion == "4":
            input_titulo = input("Ingrese el título a buscar: ").strip().lower()
            mostrar_peliculas(busqueda_lineal(peliculas, input_titulo, opcion='titulo'))
        elif opcion == "5":
            input_categoria = input("Ingrese el genero a buscar: ").strip().lower()
            mostrar_peliculas(busqueda_lineal(peliculas, input_categoria, opcion='genero'))
        elif opcion == "6":
            input_categoria = validacion('año')
            mostrar_peliculas(busqueda_lineal(peliculas, input_categoria, opcion='año'))
        elif opcion == "7":
            input_categoria = input("Ingrese la categoría que desea buscar por búsqueda binaria: ").strip().lower()
            eleccion_categoria = validacion(input_categoria)
            
            mostrar_peliculas(busqueda_binaria(peliculas, input_categoria, eleccion_categoria))
        elif opcion == "8":
            input_generos = input("Ingrese los géneros que le interesan separados por espacios: ").strip().lower()
            mostrar_peliculas(algo_recomendaciones(peliculas, input_generos))
        elif opcion == "9":
            print("¡Hasta luego! 👋")
            break       
        else:
            print("❌ Opción no válida. Por favor seleccione un número del 1 al 8.")

if __name__ == "__main__":
    main()