from .mostrar_datos import mostrar_todos_estudiantes
from .formateos import convertir_a_minusculas, quitar_espacios



def ordenar_por_promedio(notas:list, estudiantes: list, generos: list, legajos:list, estados: list, promedios: list): 
    """
    Ejecuta las funciones de ordenamiento y de mostrar datos de los estudiantes según su promedio de mayor a menor.

    Entrada:
    notas: list
    estudiantes: list
    generos: list
    legajos: list
    estados: list
    promedios: list
    Salida:
    Sin salida
    """
    if (len(promedios) == 0):
        print("Primero debe calcular los promedios")
        return
    print(promedios)
    ordenar_por_promedio_dec(notas, estudiantes, generos, legajos, estados, promedios)
    mostrar_todos_estudiantes(notas, estudiantes, generos, estados, legajos, promedios)
    
    # while True:
    #     orden = input("Ingrese 'A' para ordenar de menor a mayor o 'D' para ordenar de mayor a menor: ")
    #     orden = convertir_a_minusculas(quitar_espacios(orden))
    #     if orden == 'a':
    #         ordenar_por_promedio_segun_entrada(notas, estudiantes, generos, legajos, estados, promedios, True)
    #         mostrar_todos_estudiantes(notas, estudiantes, generos, estados, legajos, promedios)
    #         break
    #     elif orden == 'd':
    #         ordenar_por_promedio_segun_entrada(notas, estudiantes, generos, legajos, estados, promedios, False)
    #         mostrar_todos_estudiantes(notas, estudiantes, generos, estados, legajos, promedios)
    #         break
    #     else:
    #         print("Opción invalida. Ingrese 'A' o 'D'.")




def ordenar_por_promedio_dec(notas:list, estudiantes: list, generos: list, legajos:list, estados: list, promedios: list) -> None:
    """
    Función para ordenar los datos de los estudiantes según su promedio de forma descendente

    Entrada:
    notas: list
    estudiantes: list
    generos: list
    legajos: list
    estados: list
    promedios: list
    Salida:
    Sin salida
    """
    cant_promedios = len(promedios)
    for i in range(cant_promedios):
        for j in range(cant_promedios - i - 1 ):
            if promedios[j] < promedios[j + 1]:
                aux_promedio = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = aux_promedio

                aux_notas = notas[j]
                notas[j] = notas[j + 1]
                notas[j + 1] = aux_notas

                aux_estudiante = estudiantes[j]
                estudiantes[j] = estudiantes[j + 1]
                estudiantes[j + 1] = aux_estudiante

                aux_genero = generos[j]
                generos[j] = generos[j + 1]
                generos[j + 1] = aux_genero
                
                aux_legajo = legajos[j]
                legajos[j] = legajos[j + 1]
                legajos[j + 1] = aux_legajo
                
                aux_estado = estados[j]
                estados[j] = estados[j + 1]
                estados[j + 1] = aux_estado
                

def ordenar_por_promedio_segun_entrada(notas:list, estudiantes: list, generos: list, legajos:list, estados: list, promedios: list, valor: bool) -> None:
    """
    Funcion para ordenar los datos de los estudiantes según su promedio de forma ascendente o descendente según la entrada del usuario

    Entrada:
    notas: list
    estudiantes: list
    generos: list
    legajos: list
    estados: list
    promedios: list
    valor: bool
    Salida:
    Sin salida
    
    """
    cant_promedios = len(promedios)
    for i in range(cant_promedios):
        for j in range(cant_promedios - i - 1):
            if valor and promedios[j] > promedios[j + 1] or not valor and promedios[j] < promedios[j + 1]: 
                aux_promedio = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = aux_promedio

                aux_notas = notas[j]
                notas[j] = notas[j + 1]
                notas[j + 1] = aux_notas

                aux_estudiante = estudiantes[j]
                estudiantes[j] = estudiantes[j + 1]
                estudiantes[j + 1] = aux_estudiante

                aux_genero = generos[j]
                generos[j] = generos[j + 1]
                generos[j + 1] = aux_genero
                
                aux_legajo = legajos[j]
                legajos[j] = legajos[j + 1]
                legajos[j + 1] = aux_legajo
                
                aux_estado = estados[j]
                estados[j] = estados[j + 1]
                estados[j + 1] = aux_estado
               

