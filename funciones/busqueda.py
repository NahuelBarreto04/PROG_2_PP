from .validaciones import es_entero
from .formateos import quitar_espacios
from .mostrar_datos import mostrar_estudiante, mostrar_conteo_notas_repetidas_en_materia

def buscar_estudiante_por_legajo(notas:list, estudiantes:list, generos:list, estados:list, legajos:list, promedios:list) -> None:
     while True:
                legajo = input("Ingrese el número de legajo del estudiante: ")
                legajo = quitar_espacios(legajo)
                if not es_entero(legajo) or int(legajo) < 0:
                    print("Ha ingresado dato inválido. Ingrese numero de legajo.")
                    continue
                indice_legajo = 0
                for i in range(len(legajos)):
                    if int(legajo) == legajos[i]:
                        indice_legajo = i
                        break
                if legajos[indice_legajo] == int(legajo):
                    mostrar_estudiante(indice_legajo, notas, estudiantes, generos, estados, legajos, promedios)
                    break
                else:
                    print(f"No se encontró ningún estudiante con el legajo {legajo}.")
                    


    

def buscar_notas_repetidas(notas:list) -> None:
    """
    Funcion para buscar la cantidad de veces que se repiten las notas en cada materia

    Entrada:
    notas:list
    Salida:
    Sin salida


    """
    cantidad_estudiantes = len(notas)
    cantidad_materias = len(notas[0])
    
    for materia in range(cantidad_materias):
        lista_notas_materia = [] 
        
        for estudiante in range(cantidad_estudiantes):
            lista_notas_materia += [notas[estudiante][materia]]
        
        
        notas_materia = []
        conteo_nota_veces_repetida = []
        
        for nota in lista_notas_materia:
            encontrada = False
            for i in range(len(notas_materia)):
                if notas_materia[i] == nota:
                    conteo_nota_veces_repetida[i] += 1
                    encontrada = True
                    break
            
            if not encontrada:
                notas_materia += [nota]
                conteo_nota_veces_repetida += [1]
        print("")
        mostrar_conteo_notas_repetidas_en_materia(materia, lista_notas_materia, notas_materia, conteo_nota_veces_repetida)
        # print(f"Conteo de calificaciones en MATERIA_{materia + 1}:")
        # for i in range(len(notas_materia)):
        #     print(f"Calificación {notas_materia[i]}: se repite {conteo_veces_repetida[i]} vez/veces")


