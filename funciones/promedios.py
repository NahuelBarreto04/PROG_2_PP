


def crear_lista_promedios(notas: list) -> list:
    """
    Modificar la lista con los promedios de todos los estudiantes

    Entrada:
    notas: list
    Salida:
    Sin Salida
    """
    promedios = []
    for estudiante_notas in notas:
        promedio = calcular_promedio_estudiante(estudiante_notas)
        promedios += [promedio]

    return promedios



def calcular_promedio_estudiante(notas: list) -> float:
    """
    Calcula el promedio de las notas de un estudiante
    Entrada:
    notas: list - Lista con las notas del estudiante
    Salida:
    float - Promedio del estudiante
    """
    if len(notas) != 5:
        return 0.0
    
    suma = 0
    for nota in notas:
        suma += nota
    
    return suma / 5





def calcular_promedio_materia(notas:list) -> list:
    """
    Calcula el promedio de cada materia

    Entrada:
    notas: list    
    Salida:
    promedios_materias: list
    """
    promedios_materias = []
    cantidad_estudiantes = len(notas)
    cantidad_materias = len(notas[0])
    if cantidad_estudiantes == 0:
        print("No hay estudiantes cargados, debe cargar estudiantes (Opcion 1)")
        return []
    
    for materia in range(cantidad_materias):
        suma_materia = 0
        # print("materia:", materia)
        for estudiante in range(cantidad_estudiantes):
            # print("estudiante:", estudiante, "materia:", materia)
            suma_materia += notas[estudiante][materia]
        promedio_materia = suma_materia / cantidad_estudiantes
        promedios_materias += [promedio_materia]
    
    return promedios_materias
    
    



def encontrar_materias_max_promedio(promedios_materias: list) -> list:
    """
    Función para encontrar el valor máximo en una lista de números enteros

    Entrada:
    lista: list
    Salida:
    sin salida
    """
    indices_max = []
    max_promedio = promedios_materias[0]
    for i in range(1, len(promedios_materias)):
        if promedios_materias[i] > max_promedio:
            max_promedio = promedios_materias[i]

    for i in range(len(promedios_materias)):
        if promedios_materias[i] == max_promedio:
            indices_max += [i]
    # print(indices_max)
    # print(max_promedio)
    return indices_max








