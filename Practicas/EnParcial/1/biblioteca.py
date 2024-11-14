def contar_palabras(texto):
    """Cuenta el número de palabras en el texto"""
    return len(texto.split())

def contar_caracteres(texto):
    """Cuenta el número de caracteres en el texto"""
    return len(texto)

def contar_lineas(texto):
    """Cuenta el número de líneas en el texto"""
    return texto.count('\n') + 1 if texto else 0
