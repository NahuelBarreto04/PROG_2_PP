from .formateos import convertir_a_minusculas, quitar_espacios
from .validaciones import es_string


def consultar_al_usuario(mensaje: str) -> bool:
    """
    Funcion para consultar al usuario si desea continuar con una acción

    Entrada: 
    mensaje: str
    Salida: 
    continuar: bool    
    """
    input_continuar = input(mensaje)
    input_continuar = convertir_a_minusculas(input_continuar)
    input_continuar = quitar_espacios(input_continuar)
    continuar = False

    while not es_string(input_continuar) or input_continuar != "y" and input_continuar != "n":
        input_continuar = input(mensaje)
        input_continuar = convertir_a_minusculas(input_continuar)
        input_continuar = quitar_espacios(input_continuar)

    if input_continuar == "y":  
        continuar = True
        
    elif input_continuar == "n":
        continuar = False    

    return continuar



