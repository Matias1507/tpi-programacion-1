# ===================================================
# TRABAJO PRÁCTICO INTEGRADOR - PROGRAMACIÓN 1
# INTEGRANTES: Matias y Rolando
# ===================================================

# 2. Menú principal - (Rolando/Matias)
# Usar un while True con opciones numeradas.
# Validar que el usuario ingrese números válidos.

from funciones import (
    cargar_paises, 
    mostrar_paises, 
    agregar_pais, 
    actualizar_pais, 
    estadisticas, 
    buscar_pais, 
    ordenar_paises,
    filtrar_por_continente,
    eliminar_pais,
    guardar_paises
)

def menu():
    paises = cargar_paises("paises.csv")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Mostrar países")
        print("2. Agregar país")
        print("3. Actualizar datos")
        print("4. Estadísticas")
        print("5. Buscar país")
        print("6. Ordenar países por población")
        print("7. Filtrar por continente")
        print("8. Eliminar país")
        print("9. Guardar cambios en CSV")
        print("10. Salir")

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
            buscar_pais(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            filtrar_por_continente(paises)
        elif opcion == "8":
            eliminar_pais(paises)
        elif opcion == "9":
            guardar_paises("paises.csv", paises)
        elif opcion == "10":
            guardar_paises("paises.csv", paises)
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
