# busqueda.py - Búsqueda secuencial de un expediente por su código.
import datos


def buscarExpediente(codigoBuscado):
    """Devuelve la posición del expediente o -1 si no existe."""
    for i in range(len(datos.codigos)):
        if datos.codigos[i] == codigoBuscado:
            return i
    return -1
