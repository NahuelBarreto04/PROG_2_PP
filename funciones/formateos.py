def convertir_a_minusculas(cadena:str):
    """
    Funcion para convertir una cadena a minusculas
    Entrada:
    cadena: str
    Salida:
    cadena_resultado: str
    """
    cadena_resultado = ""

    for i in range(len(cadena)):
        valor_asci = ord(cadena[i])

        if  valor_asci  >= 65 and valor_asci <= 90:
            valor_asci = valor_asci + 32
            cadena_resultado += chr(valor_asci)
        else:
            cadena_resultado += cadena[i]

    return cadena_resultado

def quitar_espacios(cadena:str):
    """
    Funcion para quitar los espacios en blanco de una cadena
    
    Entrada:
    cadena: str
    Salida:
    cadena_resultado: str
    """
    cadena_resultado = ""

    for i in range(len(cadena)):
        if cadena[i] != " ":
            cadena_resultado += cadena[i]

    return cadena_resultado



def convertir_primera_mayuscula(cadena:str):
    """
    Funcion para convertir la primera letra de la cadena en Mayuscula y las otras en minusculas

    Entrada:
    cadena: str
    Salida:
    cadena_resultado: str
    """
    cadena_resultado = ""
    if cadena != "":
        primera_letra = cadena[0]
        ascci_primera_letra = ord(primera_letra)

        if ascci_primera_letra >= 97 and ascci_primera_letra <= 122:
            ascci_primera_letra = ascci_primera_letra - 32
            cadena_resultado += chr(ascci_primera_letra)
        else:
            cadena_resultado += primera_letra

        for i in range(1, len(cadena)):
            letra = cadena[i]
            ascii_letra = ord(letra)

            if ascii_letra >= 65 and ascii_letra <= 90:
                ascii_letra = ascii_letra + 32
                cadena_resultado += chr(ascii_letra)
            else:
                cadena_resultado += cadena[i]
    else:
        cadena_resultado = cadena
    return cadena_resultado

