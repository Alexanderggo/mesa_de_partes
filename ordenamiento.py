# ordenamiento.py - Ordenamiento por inserción sobre arreglos paralelos.
import datos


def clave(i, criterio):
    """Valor por el que se compara el expediente i.
    Fecha: se reordena 'dd/mm/aaaa hh:mm' como 'aaaammddhhmm' para comparar cadenas."""
    if criterio == "fecha":
        f = datos.fechas[i]
        return f[6:10] + f[3:5] + f[0:2] + f[11:13] + f[14:16]
    return datos.codigos[i]


def moverExpediente(origen, destino):
    """Copia todos los campos de la posición origen a la posición destino."""
    datos.codigos[destino] = datos.codigos[origen]
    datos.dnis[destino] = datos.dnis[origen]
    datos.nombres[destino] = datos.nombres[origen]
    datos.tipos[destino] = datos.tipos[origen]
    datos.asuntos[destino] = datos.asuntos[origen]
    datos.folios[destino] = datos.folios[origen]
    datos.fechas[destino] = datos.fechas[origen]
    datos.estados[destino] = datos.estados[origen]


def ordenarExpedientes(criterio):
    """Ordena de forma ascendente por 'fecha' o 'codigo' (método de inserción)."""
    for i in range(1, len(datos.codigos)):
        # Guardar el expediente i en variables auxiliares
        aux = [datos.codigos[i], datos.dnis[i], datos.nombres[i], datos.tipos[i],
               datos.asuntos[i], datos.folios[i], datos.fechas[i], datos.estados[i]]
        claveAux = clave(i, criterio)
        j = i - 1
        while j >= 0 and clave(j, criterio) > claveAux:
            moverExpediente(j, j + 1)
            j = j - 1
        # Colocar el expediente auxiliar en su posición
        datos.codigos[j + 1] = aux[0]
        datos.dnis[j + 1] = aux[1]
        datos.nombres[j + 1] = aux[2]
        datos.tipos[j + 1] = aux[3]
        datos.asuntos[j + 1] = aux[4]
        datos.folios[j + 1] = aux[5]
        datos.fechas[j + 1] = aux[6]
        datos.estados[j + 1] = aux[7]
