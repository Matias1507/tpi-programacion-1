
# 1. Lectura del archivo CSV 
# Crear una función que abra paises.csv.
# Leerlo línea por línea con csv.reader.
# Convertir población y superficie a enteros con try/except.
import csv

def cargar_paises(nombre_archivo):
    paises = []
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
            except ValueError:
                print(f"Error al convertir datos de {fila['nombre']}")
    return paises

# 2. Mostrar países
# Imprime todos los países cargados:
def mostrar_paises(paises):
    print("\n--- LISTA DE PAÍSES ---")
    for pais in paises:
        print(f"{pais['nombre']} - {pais['continente']} - Población: {pais['poblacion']} - Superficie: {pais['superficie']}")

# 3. Agregar país (Alta)
# Permite sumar un país nuevo validando que no haya campos vacíos:
def agregar_pais(paises):
    nombre = input("Nombre del país: ").strip()
    continente = input("Continente: ").strip()
    poblacion = input("Población: ").strip()
    superficie = input("Superficie: ").strip()

    if not nombre or not continente or not poblacion or not superficie:
        print("Error: no se permiten campos vacíos.")
        return

    try:
        paises.append({
            "nombre": nombre,
            "continente": continente,
            "poblacion": int(poblacion),
            "superficie": int(superficie)
        })
        print(f"País {nombre} agregado correctamente.")
    except ValueError:
        print("Error: población y superficie deben ser números.")

# 4. Actualizar datos
# Busca un país y modifica población o superficie:
def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            campo = input("¿Qué desea actualizar? (poblacion/superficie): ").strip().lower()
            if campo in ["poblacion", "superficie"]:
                nuevo_valor = input(f"Ingrese nuevo valor para {campo}: ")
                try:
                    pais[campo] = int(nuevo_valor)
                    print(f"{campo} de {nombre} actualizado correctamente.")
                except ValueError:
                    print("Error: debe ingresar un número.")
            else:
                print("Campo inválido.")
            return
    print("País no encontrado.")

# 5. Estadísticas
# Calcula mayor/menor población, promedios y cantidad por continente:
def estadisticas(paises):
    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)

    print("\n--- ESTADÍSTICAS ---")
    print(f"Mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"Menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio población: {promedio_poblacion:.2f}")
    print(f"Promedio superficie: {promedio_superficie:.2f}")

    # Cantidad de países por continente
    continentes = {}
    for p in paises:
        continentes[p["continente"]] = continentes.get(p["continente"], 0) + 1
    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"{cont}: {cant}")
# 6. Buscar país 
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

# 7. Ordenar países 
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

# 8. Eliminar país (Baja) 
# Busca un país por nombre y lo remueve de la lista del sistema:
def eliminar_pais(paises):
    nombre = input("Ingrese el nombre del país a eliminar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            paises.remove(pais)
            print(f"País {pais['nombre']} eliminado correctamente.")
            return
    print("País no encontrado.")

# 9. Guardar cambios en CSV 
# Sobreescribe el archivo paises.csv con los datos actuales de la lista:
def guardar_paises(nombre_archivo, paises):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)
    print("Cambios guardados en el archivo CSV correctamente.")
