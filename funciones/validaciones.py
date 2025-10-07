

def es_entero(cadena):
    """
    Funcion para validar si una cadena es un entero
    
    Entrada:
    cadena: str
    Salida:
    es_digito: bool
    """
    signo = 0
    primer_caracter = cadena[0]
    ascii_mas = 43
    ascii_menos = 45
    es_digito = True

    if ord(primer_caracter) == ascii_menos or ord(primer_caracter) == ascii_mas:
        signo = 1
    
    ascii_cero = 48
    ascii_nueve = 57

    for i in range(signo, len(cadena)):
        digito = cadena[i]
        digito_ascii = ord(digito)

        if digito_ascii < ascii_cero or digito_ascii > ascii_nueve:
            es_digito = False
            break
    
    return es_digito


def es_string(cadena):
    """
    Funcion para validar si una cadena es un string

    Entrada:
    cadena: str
    Salida:
    es_string: bool 
    """
    es_string = True

    for i in range(len(cadena)):
        valor_asci = ord(cadena[i])
        es_valido = (valor_asci == 32) or \
                    (valor_asci >= 65 and valor_asci <= 90) or \
                    (valor_asci >= 97 and valor_asci <= 122)

        if not es_valido:
            es_string = False
            break

    return es_string
