# validaciones.py - Funciones que revisan los datos antes de registrarlos.
from datos import TIPOS_PERMITIDOS


def validarDNI(dni):
    """Verdadero si el DNI tiene exactamente 8 caracteres y todos son dígitos."""
    return len(dni) == 8 and dni.isdigit()


def validarTipo(tipo):
    """Verdadero si el tipo de documento está entre los permitidos."""
    return tipo in TIPOS_PERMITIDOS


def validarDatos(nombre, asunto, folios):
    """Verdadero si los textos no están vacíos y los folios son un entero > 0."""
    if nombre == "" or asunto == "":
        return False
    return folios.isdigit() and int(folios) > 0
