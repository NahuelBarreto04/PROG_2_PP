from funciones.carga_de_datos import cargar_datos
from funciones.mostrar_datos import mostrar_estudiantes, mostrar_materias_con_mayor_promedio
from funciones.promedios import crear_lista_promedios
from funciones.ordenamiento import ordenar_por_promedio
from funciones.busqueda import buscar_estudiante_por_legajo, buscar_notas_repetidas
Init = True


lista_notas = []
lista_estudiantes = []
lista_generos = []
lista_estados = []
lista_legajos = []
lista_promedios = []

# lista_notas = [[8, 7, 6, 9, 8], [5, 6, 7, 5, 6], [9, 10, 8, 9, 9], [7, 8, 7, 6, 8], [6, 5, 7, 6, 5]]
# lista_estudiantes = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Luisa Rodríguez"]
# lista_generos = ["M", "F", "M", "F", "F"]
# lista_estados = [1, 1, 1, 0, 1]
# lista_legajos = [123456, 234567, 345678, 456789, 567890]
# lista_promedios = []

while Init:
    print("")
    print("--- Menú Principal ---")
    print("1. Realizar carga de Estudiantes")
    print("2. Mostrar todos los datos de los estudiantes o estudiante")
    print("3. Calcular promedio de cada estudiante")
    print("4. Ordenar y mostrar los datos de los estudiantes por promedio")
    print("5. Mostrar la/s materia/s con mayor promedio general")
    print("6. Buscar y mostrar todos los datos de un estudiante por legajo")
    print("7. Buscar y mostrar cuantas veces se repite cada calificación en una asignatura determinada")
    print("8. Salir del sistema")
    print("")
    input_user_option = (input("Ingrese la opcion a realizar: "))
    ingreso_caso_1 = [False]
    # valid_input = validate_number(input_user_option)

    # while not valid_input:
    #     print("Por favor ingrese el número correcto de la opción a ejecutar")
    #     input_user_option = (input("Ingrese la opcion a realizar: "))
    #     valid_input = validate_number(input_user_option)


    match input_user_option:
        case "1":
            print("--- Carga de Estudiantes ---")  
            cargar_datos(lista_notas, lista_estudiantes, lista_generos,lista_legajos, lista_estados)
        case "2":
            mostrar_estudiantes(lista_notas, lista_estudiantes, lista_generos,lista_estados, lista_legajos)
        case "3":
            lista_promedios = crear_lista_promedios(lista_notas)
        case "4":
            ordenar_por_promedio(lista_notas,lista_estudiantes,lista_generos,lista_legajos,lista_estados,lista_promedios)
        case "5":
            mostrar_materias_con_mayor_promedio(lista_notas)
        case "6":
            buscar_estudiante_por_legajo(lista_notas, lista_estudiantes, lista_generos,lista_estados, lista_legajos, lista_promedios)
        case "7":
            buscar_notas_repetidas(lista_notas)
                
        case "8":
               print("Cierre de sistema")
               Init = False