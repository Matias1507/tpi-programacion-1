# ===================================================
# TRABAJO PRÁCTICO INTEGRADOR - PROGRAMACIÓN 1
# INTEGRANTES: Matias y Rolando
# ===================================================

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
    # El paso 1 (Cargar países) se ejecuta automáticamente al iniciar el sistema
    paises = cargar_paises("paises.csv")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("2. Mostrar países")
        print("3. Agregar país (Alta)")
        print("4. Actualizar datos")
        print("5. Estadísticas e Indicadores")
        print("6. Buscar país")
        print("7. Ordenar países por población")
        print("8. Filtrar por continente")
        print("9. Eliminar país (Baja)")
        print("10. Guardar cambios en CSV")
        print("11. Salir")

        opcion = input("Elija una opción (2-11): ").strip()

        if opcion == "2":
            mostrar_paises(paises)
        elif opcion == "3":
            agregar_pais(paises)
        elif opcion == "4":
            actualizar_pais(paises)
        elif opcion == "5":
            estadisticas(paises)
        elif opcion == "6":
            buscar_pais(paises)
        elif opcion == "7":
            ordenar_paises(paises)
        elif opcion == "8":
            filtrar_por_continente(paises)
        elif opcion == "9":
            eliminar_pais(paises)
        elif opcion == "10":
            guardar_paises("paises.csv", paises)
        elif opcion == "11":
            # Guardamos automáticamente por seguridad antes de cerrar
            guardar_paises("paises.csv", paises)
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
