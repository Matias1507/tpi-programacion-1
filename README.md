# Trabajo Práctico Integrador - Programación 1

## Sistema de Gestión de Países (Python)
**UTN - Tecnicatura Universitaria en Programación**

Este es nuestro proyecto final para la materia Programación 1. Es un programa de consola interactivo hecho en Python que lee una base de datos de países desde un archivo CSV y permite gestionarlos (dar de alta, modificar, borrar, buscar, filtrar por continente y ver estadísticas).

---

### Integrantes
* Walter Matias Kurtz
* Rolando Alanis

---

### Enlaces del Proyecto (Obligatorios)

* **Video de la defensa en YouTube:** [Link al video acá](AGREGAR_LINK_DEL_VIDEO)
* **Informe técnico en PDF:** [Descargar PDF](./Consigna_TPI_Prog-1.docx.pdf)

---

### Reparto de tareas en el código

Para organizarnos el trabajo, nos dividimos las funciones del sistema de la siguiente manera:

**Desarrollado por Rolando:**
* Carga inicial de los datos desde el archivo `paises.csv` usando manejo de errores (try/except).
* Mostrar la lista completa de todos los países en pantalla.
* Agregar un país nuevo a la lista validando que no queden campos vacíos.
* Modificar los datos (población o superficie) de un país ya existente.
* Pantalla de estadísticas (país con más y menos habitantes, promedios generales y cantidad de países por continente).

**Desarrollado por Matias:**
* Buscar un país específico por su nombre y mostrar su ficha de datos.
* Ordenamiento de los países de menor a mayor por cantidad de población, usando el método Burbuja clásico con variable auxiliar.
* Filtrar y mostrar en consola únicamente los países que pertenecen a un continente ingresado.
* Eliminar un país de la lista.
* Guardar los cambios definitivos de vuelta en el archivo CSV al actualizar o salir del programa.

---

### Archivos del repositorio

* `main.py`: Tiene el código del menú principal con las opciones del 1 al 10 y el bucle while para que funcione el programa.
* `funciones.py`: Tiene toda la lógica y los bloques de código de cada función que creamos.
* `paises.csv`: El archivo de texto plano con los datos de los países que usa el programa.

---

### Cómo ejecutar el programa

El sistema se armó usando únicamente librerías estándar de Python 3, por lo que no hace falta instalar nada raro.

1. Clonar el repositorio:
   git clone https://github.com/Matias1507/tpi-programacion-1.git

2. Entrar a la carpeta:
   cd tpi-programacion-1

3. Correr el archivo principal:
   python main.py
