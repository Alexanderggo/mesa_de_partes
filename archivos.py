# archivos.py - Persistencia: lee y escribe expedientes.txt (un expediente por línea, campos separados por ';').
import os
import datos

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), datos.ARCHIVO)


def guardarExpedientes():
    with open(RUTA, "w", encoding="utf-8") as f:
        for i in range(len(datos.codigos)):
            linea = ";".join([datos.codigos[i], datos.dnis[i], datos.nombres[i],
                              datos.tipos[i], datos.asuntos[i], str(datos.folios[i]),
                              datos.fechas[i], datos.estados[i]])
            f.write(linea + "\n")


def cargarExpedientes():
    """Carga el archivo al iniciar. Si no existe todavía, empieza con el registro vacío."""
    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            for linea in f:
                campos = linea.strip().split(";")
                if len(campos) != 8:      # línea dañada: se omite
                    continue
                datos.codigos.append(campos[0])
                datos.dnis.append(campos[1])
                datos.nombres.append(campos[2])
                datos.tipos.append(campos[3])
                datos.asuntos.append(campos[4])
                datos.folios.append(int(campos[5]))
                datos.fechas.append(campos[6])
                datos.estados.append(campos[7])
    except FileNotFoundError:
        print("(No hay expedientes guardados todavía.)")
