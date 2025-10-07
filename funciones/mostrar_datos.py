
from .validaciones import es_entero
from .formateos import quitar_espacios
from .promedios import calcular_promedio_materia, encontrar_materias_max_promedio
def mostrar_estudiantes(notas:list, estudiantes:list, generos:list, estados:list, legajos:list) -> None:
     while True:
        """
        Función general que ejecuta las funciones para mostrar los datos de los estudiantes

        Entrada:
        notas: list
        estudiantes: list
        generos: list
        estados: list
        legajos: list
        promedios: list
        Salida:
        Sin salida
        """

        # if len(estudiantes) == 0:
        #     print("No hay estudiantes cargados. Primero debe cargar estudiantes (Opcion 1).")
        #     break

        print("Desea mostrar todos los estudiantes o uno en particular?")
        print("1. Todos")
        print("2. Uno en particular")
        opcion = input("Ingrese la opción (1/2): ")
        if opcion == "1":
            mostrar_todos_estudiantes(notas, estudiantes, generos, estados,legajos, [0])
            break
        elif opcion == "2":
            while True:
                indice = input("Ingrese el numero de estudiante que quiere ver: ")
                indice = quitar_espacios(indice)
                indice_estudiante = int(indice) - 1
                if not es_entero(indice) or indice_estudiante < 0 or indice_estudiante >= len(estudiantes):
                    print(f"El numero de estudiante {indice} no existe. Ingrese un numero valido.")
                    print(f"Estudiantes disponibles: 1 a {len(estudiantes)}")
                    continue
                
                mostrar_estudiante(indice_estudiante, notas, estudiantes, generos, estados, legajos, [0])
                break
        break





def mostrar_todos_estudiantes(notas: list, estudiantes: list, generos: list, estados: list,legajos:list, promedios:list) -> None:
    """
    Función para mostrar todos los datos de los estudiantes

    Entrada:
    notas: list
    estudiantes: list
    generos: list
    estados: list
    legajos: list
    promedios: list
    Salida:
    Sin salida

    """
    print("Datos de los estudiantes:")

    for i in range(len(estudiantes)):
        if estados[i] == 1:  
            print(f"Legajo: {legajos[i]}", end=" - ")
            print(f"Estudiante: {estudiantes[i]}", end=" - ")
            print(f"Género: {generos[i]}", end=" - ")
            print(f"Estado: Activo", end=" - ")
            print("Notas: ", end="")
            for nota in range(len(notas[i])):
                if nota == len(notas[i]) - 1:
                    print(f"{notas[i][nota]}", end="")
                else:
                    print(f"{notas[i][nota]}", end=", ")
            if len(promedios) > 1:
                print(f" Promedio: {promedios[i]}", end="")
            print("")


def mostrar_estudiante(indice:int, notas: list, estudiantes: list, generos: list, estados: list, legajos:list, promedios:list) -> None:
    """
    Muestra los datos de un estudiante especifico si esta activo

    Etrada:
    indice: int
    notas: list
    estudiantes: list
    generos: list
    estados: list
    legajo: list
    promedios: list

    Salida:
    Sin salida


    """
    if estados[indice] == 1:
        print(f"Estudiante {indice + 1}", end=" - ")
        print(f"Legajo: {legajos[indice]}", end=" - ")
        print(f"Nombre: {estudiantes[indice]}", end=" - ")
        print(f"Género: {generos[indice]}", end=" - ")
        for nota in range(len(notas[indice])):
            if nota == len(notas[indice]) - 1:
                print(f"{notas[indice][nota]}", end="")
            else:
                print(f"{notas[indice][nota]}", end=", ")
        if len(promedios) > 1:
            print(f" - Promedio: {promedios[indice]}", end="")
            print("")

    else:
        print(f"El estudiante {indice} está inactivo")




def mostrar_materias_con_mayor_promedio(notas: list) -> None:
    """
    Muestra la/s materia/s con mayor promedio

    Entrada:
    promedios_materias: list
    Salida:
    Sin salida
    """
    
    promedios = calcular_promedio_materia(notas)
    # print(promedios)
    indices_max = encontrar_materias_max_promedio(promedios)
    # print(indices_max)
    print("El promedios de las materias es:")
    mostrar_todas_las_materias(promedios)
    print("Las materias con mayor promedio general son: ")
    max_promedio = promedios[indices_max[0]]
    for indice in indices_max:
            mostrar_materia(indice, max_promedio)



def mostrar_materia(indice: int, promedio: float)-> None:
    """
    Muestra una materia con su nombre y promedio
    
    Entrada:
    indice:int
    promedio: float
    Salida:
    Sin salida
    """
    nombre_materia = f"MATERIA_{indice + 1}"
    print(f"{nombre_materia}: {promedio}: ")

def mostrar_todas_las_materias(promedios:list) -> None:
    """
    Función para recorrer TODAS las materias y mostrarlas
    
    Entrada:
    promedios:list
    Salida:
    Sin salida
    """
    
    for i in range(len(promedios)):
        mostrar_materia(i, promedios[i])

    


def mostrar_conteo_notas_repetidas_en_materia(materia:int, lista_notas_materia: list, notas_materia: list, conteo_nota_veces_repetida:list) -> None:
    """
    Funcion para mostrar los datos del conteo de notas repetidas en una misma materia

    Entrada:
    materia: int
    lista_notas_materia:list
    notas_materia: list
    conteo_veces_repetida:list
    Salida:
    Sin Salida
    """
    print(f"Materia MATERIA_{materia + 1}:")
    print(f"Todas las notas: {lista_notas_materia}")
    print("Conteo de veces repetidas de las notas en la materia:")
    for i in range(len(notas_materia)):
        print(f"Calificación {notas_materia[i]}: se repite {conteo_nota_veces_repetida[i]} vez/veces")