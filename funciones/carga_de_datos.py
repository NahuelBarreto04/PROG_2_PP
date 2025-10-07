from .validaciones import es_entero, es_string
from .utiles import consultar_al_usuario
from .formateos import convertir_primera_mayuscula, quitar_espacios

def cargar_datos(notas: list, estudiantes: list, generos: list,legajos:list, estados: list) -> None:
    """
    Función para realizar la carga de los datos principales

    Entrada:
    notas: list
    estudiantes: list
    generos: list
    legajos: list
    estados: list
    Salida:
    Sin salida
    """
    
    while True:
        if len(notas) >= 30:
            print("Ya ha ingresado el limite de estudiantes (30)")
            break
        
        cargar_notas(notas)
        cargar_estudiantes(estudiantes)
        cargar_genero(generos)
        cargar_legajo(legajos)
        cargar_estado(estados)
        
        
        mensaje = "¿Desea cargar otro estudiante? (y/n): "
        if not consultar_al_usuario(mensaje):
            break
    
    print(f"Carga Hecha")







def cargar_notas(notas: list) -> None:
    """"
    Función para cargar las notas de un estudiante modificando la lista de notas

    Entrada:
    notas: list
    Salida:
    Sin salida
    """
    local_notas = [0,0,0,0,0]
    for nota in range(5):
        nota_input = input(f"Ingrese la nota (1 a 10): ")
        while not es_entero(nota_input) or int(nota_input) < 1 or int(nota_input) > 10:
            print("El valor ingresado no es valido, ingrese un número válido")
            nota_input = input(f"Ingrese la nota (1 a 10): ")
        print(nota_input, local_notas)
        local_notas[nota] = int(nota_input)
    notas += [local_notas]
    print(notas)


# def cargar_notas(notas: list) -> None:
#     try:
#       codigo
#     except Exception as e:
#         print(f"ERROR en cargar_notas: {e}")




def cargar_estudiantes(estudiantes: list) -> None:
    """
    Función para cargar el nombre y apellido del estudiante  modificando la lista de estudiantes

    Entrada:
    estudiantes: list
    Salida:
    Sin salida
    """
    nombre = input("Ingrese el nombre del estudiante: ")
    nombre = convertir_primera_mayuscula(quitar_espacios(nombre))
    while not es_string(nombre) or nombre == "":
        print("El valor ingresado no es valido, ingrese un texto válido")
        nombre = input("Ingrese el nombre del estudiante: ")
        nombre = convertir_primera_mayuscula(quitar_espacios(nombre))


    apellido = input("Ingrese el apellido del estudiante: ")
    apellido = convertir_primera_mayuscula(quitar_espacios(apellido))
    while not es_string(apellido) or apellido == "":
        print("El valor ingresado no es valido, ingrese un texto válido")
        apellido = input("Ingrese el apellido del estudiante: ")
        apellido = convertir_primera_mayuscula(quitar_espacios(apellido))
  

    estudiante = [f"{nombre} {apellido}"]
    estudiantes += estudiante
    print(estudiantes)



def cargar_genero(generos: list) -> None:
    """
    Función para cargar el género del estudiante modificando la lista de géneros

    Entrada:
    generos: list
    Salida:
    Sin salida
    """
    genero = input("Ingrese el género del estudiante (M | F | X): ")
    genero = convertir_primera_mayuscula(quitar_espacios(genero))
    while not es_string(genero) or genero != "M" and genero != "F" and genero != "X":
        print("El valor ingresado no es valido, ingrese un texto válido")
        genero = input("Ingrese el género del estudiante (M | F | X): ")
        genero = convertir_primera_mayuscula(quitar_espacios(genero))
  
    generos += genero
    print(generos)

def cargar_legajo(legajos: list) -> None:
    """
    Función para cargar el legajo del estudiante modificando la lista de legajos

    Entrada:
    legajos: list
    Salida:
    Sin salida
    """
    while True:
        legajo = input("Ingrese el legajo del estudiante (6 cifras): ")
        legajo = quitar_espacios(legajo)
        if not es_entero(legajo) or len(legajo) != 6:
            print("El valor ingresado no es valido, ingrese un número de 6 cifras")
            continue

        legajo = int(legajo)
        repetido = False

        for i in range(len(legajos)):
            if legajo == legajos[i]:
                print("El legajo ingresado ya existe, por favor ingrese otro")
                repetido = True
                break
        
        if repetido:
            continue
        
        break

    legajo = [legajo]
    legajos += legajo




def cargar_estado(estados: list) -> None:
    """
    Función para cargar el estado del estudiante modificando la lista de estados

    Entrada:
    estados: list
    Salida:
    Sin salida
    """
    while True:
        estado_input = input("Ingrese el estado del estudiante (0=Libre, 1=Ocupado): ")
        estado = quitar_espacios(estado_input)

        if not es_entero(estado) or (estado != "0" and estado != "1"):
            print("El valor ingresado no es valido, ingrese 0 para Libre o 1 para Ocupado")
            continue

        estado = int(estado)
        break
    estado = [estado]
    estados += estado







        