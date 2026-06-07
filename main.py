# ===================================================
# TRABAJO PRÁCTICO INTEGRADOR - PROGRAMACIÓN 1
# INTEGRANTES: Mati y Rolando
# ===================================================

# (LISTA DE PRUEBA)
lista_paises = [
    {"nombre": "Argentina", "poblacion": 46000000, "superficie": 2780400, "continente": "América"},
    {"nombre": "Francia", "poblacion": 68000000, "superficie": 543940, "continente": "Europa"},
    {"nombre": "Japón", "poblacion": 125000000, "superficie": 377975, "continente": "Asia"},
    {"nombre": "Brasil", "poblacion": 214000000, "superficie": 8515767, "continente": "América"}
]

for pais in lista_paises:
    print(pais["nombre"])