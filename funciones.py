import csv

# 5. Estadísticas e Indicadores - (Rolando)
# Genera el reporte analítico calculando extremos, promedios y distribución por continente de forma manual:
def estadisticas(paises):
    # Validación de seguridad por si la lista está vacía
    if not paises:
        print("No hay países registrados para calcular estadísticas.")
        return

    # Inicializamos variables testigo con el primer elemento de la lista (índice 0)
    # Asumimos temporalmente que el primero es el mayor, el menor y arrancamos las sumas
    pais_mayor_pob = paises[0]
    pais_menor_pob = paises[0]
    
    total_poblacion = 0
    total_superficie = 0
    
    # Diccionario acumulador dinámico para contar los países por continente
    continentes_contador = {}

    # Recorrido secuencial e iterativo de la lista principal
    for p in paises:
        # Algoritmo de búsqueda de extremos (reemplaza a max() y min() con lambda)
        if p["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = p  # Actualizamos el registro del mayor
            
        if p["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = p  # Actualizamos el registro del menor

        # Sumatorias aritméticas para determinar los promedios generales
        total_poblacion += p["poblacion"]
        total_superficie += p["superficie"]

        # Lógica del diccionario acumulador para la distribución por continente
        continente = p["continente"]
        if continente in continentes_contador:
            continentes_contador[continente] += 1
        else:
            continentes_contador[continente] = 1

    # Cálculo final de los promedios generales
    cantidad_total_paises = len(paises)
    promedio_poblacion = total_poblacion / cantidad_total_paises
    promedio_superficie = total_superficie / cantidad_total_paises

    # Despliegue de los indicadores e informes por consola
    print("\n" + "="*45)
    print("         REPORTE ESTADÍSTICO DEL SISTEMA")
    print("="*45)
    print(f"País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']} hab.)")
    print(f"País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']} hab.)")
    print("-"*45)
    print(f"Promedio de población general: {promedio_poblacion:.2f} hab.")
    print(f"Promedio de superficie general: {promedio_superficie:.2f} km²")
    print("-"*45)
    print("Distribución exacta de países por continente:")
    for cont, cant in continentes_contador.items():
        print(f" - {cont}: {cant} país(es)")
    print("="*45 + "\n")

# 6. Buscar país - (Matias)
# Busca un país específico por nombre y muestra sus datos detallados:
def buscar_pais(paises):
    nombre = input("Ingrese el nombre del país a buscar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("\n--- PAÍS ENCONTRADO ---")
            print(f"Nombre: {pais['nombre']}")
            print(f"Continente: {pais['continente']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            return
    print("País no encontrado.")

# 7. Ordenar países - (Matias)
# Ordena la lista de países por población de menor a mayor usando el método burbuja:
def ordenar_paises(paises):
    n = len(paises)
    for i in range(n):
        for j in range(0, n - i - 1):
            if paises[j]["poblacion"] > paises[j + 1]["poblacion"]:
                aux = paises[j]
                paises[j] = paises[j + 1]
                paises[j + 1] = aux
    print("\nPaíses ordenados por población de menor a mayor.")
    mostrar_paises(paises)

# 8. Filtrar por continente - (Matias)
# Muestra todos los países que pertenecen a un continente específico:
def filtrar_por_continente(paises):
    continente = input("Ingrese el continente para filtrar: ").strip()
    print(f"\n--- PAÍSES DE {continente.upper()} ---")
    encontrado = False
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(f"{pais['nombre']} - Población: {pais['poblacion']} - Superficie: {pais['superficie']}")
            encontrado = True
    if not encontrado:
        print("No se encontraron países en ese continente.")

# 9. Eliminar país (Baja) - (Matias)
# Busca un país por su nombre y lo remueve de la lista del sistema:
def eliminar_pais(paises):
    nombre = input("Ingrese el nombre del país a eliminar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            paises.remove(pais)
            print(f"País {pais['nombre']} eliminado correctamente.")
            return
    print("País no encontrado.")

# 10. Guardar cambios en CSV - (Matias)
# Sobreescribe el archivo CSV con los datos actuales de la lista:
def guardar_paises(nombre_archivo, paises):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)
    print("Cambios guardados en el archivo CSV correctamente.")
