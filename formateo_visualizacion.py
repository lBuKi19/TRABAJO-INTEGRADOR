import csv

def cargar_peliculas():
    """Carga las películas desde el archivo IMBD.csv"""
    peliculas = []  # Lista para almacenar todas las películas y series
    
    try:
        # Abrir el archivo CSV con codificación UTF-8 (para manejar caracteres especiales)
        with open('IMBDcopy.csv', 'r', encoding='utf-8') as archivo:
            # Crear un lector de CSV que mapea cada fila a un diccionario
            lector = csv.DictReader(archivo)
            # Procesar cada fila del archivo CSV
            for fila in lector:    
                try:
                    # Procesamiento del año - extraer solo los 4 dígitos numéricos
                    year_str = str(fila.get('año', '')).strip()
                    if year_str.isdigit() and len(year_str) == 4:
                        fila['año'] = int(year_str)
                    else:
                        # Extraer dígitos de cadenas como "(1994)" o "1994-01-01"
                        digits = ''.join([c for c in year_str if c.isdigit()])
                        fila['año'] = int(digits[:4]) if len(digits) >= 4 else 0
                    
                    # Procesamiento del rating - manejar diferentes formatos numéricos
                    rating_str = str(fila.get('rating', '')).strip()
                    if rating_str.replace('.', '').replace(',', '').isdigit():
                        fila['rating'] = float(rating_str.replace(',', '.'))  # Manejar decimales con coma
                    else:
                        fila['rating'] = 0.0
                    
                              
                except (ValueError, AttributeError) as e:
                    # Manejar errores en la conversión de datos
                    print(f"⚠️  Error convirtiendo datos en fila {len(peliculas)+1}: {e}")
                    fila['año'] = 0
                    fila['rating'] = 0.0
                    
                
                # Agregar la película procesada a la lista
                peliculas.append(fila)
        
        return peliculas
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'IMBDcopy.csv'")
        print("Colocar el archivo debe estar en el mismo directorio que este programa")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        return None


def mostrar_peliculas(peliculas, limite=10):
    barra_grande= '='*110
    """Mostrar películas en formato de tabla"""
    if not peliculas:
        print("No hay películas para mostrar.")
        return
    # Encabezado de la tabla
    print(f"\n{barra_grande}")
    print(f"Mostrando {min(len(peliculas), limite)} de {len(peliculas)} películas:")
    print(f"{barra_grande}")
    print(f"{'#':<3} {'TÍTULO':<40} {'AÑO':<6} {'GÉNERO':<18} {'RATING':<8}")
    print(barra_grande)
    
    # Mostrar cada elemento alineado
    for i, p in enumerate(peliculas[:limite]):
        # Acortar campos largos para mejor visualización
        titulo_pelicula = p['titulo'][:39] + '...' if len(p['titulo']) > 39 else p['titulo']
        año = str(p['año']) if p['año'] > 0 else 'N/A'
        genero = p['genero'][:17] + '...' if len(p['genero']) > 17 else p['genero']
        rating = f"{p['rating']:.1f}" if p['rating'] > 0 else 'N/A'
        
        # Imprimir fila formateada
        print(f"{i+1:<3} {titulo_pelicula:<40} {año:<6} {genero:<18} {rating:<8}")

def validacion(input_categoria):
    global eleccion
    if input_categoria == 'año':
                while True:
                    eleccion = input("Ingrese el año a buscar: ").strip()
                    if eleccion.isdigit():
                        eleccion = int(eleccion)
                        break
                    else:
                        print("❌ Por favor ingrese un año válido (número entero).")
    elif input_categoria == 'rating':
                try:
                    eleccion = float(input("Ingrese el rating: "))
                except ValueError:
                    print("❌ Por favor ingrese un rating válido(número entero o con punto).")
                    
    return eleccion