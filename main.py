# ===================================================
# TRABAJO PRÁCTICO INTEGRADOR - PROGRAMACIÓN 1
# INTEGRANTES: Mati y Rolando
# ===================================================

# (LISTA DE PRUEBA) REALIZADO POR MATI
# lista_paises = [
#     {"nombre": "Argentina", "poblacion": 46000000, "superficie": 2780400, "continente": "América"},
#     {"nombre": "Francia", "poblacion": 68000000, "superficie": 543940, "continente": "Europa"},
#     {"nombre": "Japón", "poblacion": 125000000, "superficie": 77975, "continente": "Asia"},
#     {"nombre": "Brasil", "poblacion": 214000000, "superficie": 8515767, "continente": "América"}
# ]

# for pais in lista_paises:
#     print(pais["nombre"])


# ------------------***********-----------------------


# 2. Menú principal - (Rolando)
# Usar un while True con opciones numeradas.
# Validar que el usuario ingrese números válidos.

from funciones import cargar_paises, mostrar_paises, agregar_pais, actualizar_pais, estadisticas

def menu():
    paises = cargar_paises("paises.csv")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Mostrar países")
        print("2. Agregar país")
        print("3. Actualizar datos")
        print("4. Estadísticas")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            estadisticas(paises)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()




# Prueba de ejecución
# paises = cargar_paises("paises.csv")

# for pais in paises:
#     print(pais["nombre"])


