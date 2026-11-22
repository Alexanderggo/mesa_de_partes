# datos.py - Arreglos paralelos y constantes compartidas por todos los módulos.
# La posición i de cada lista corresponde al mismo expediente.
# Importante: las listas se modifican con append() o por posición, nunca se reasignan.

codigos = []
dnis = []
nombres = []
tipos = []
asuntos = []
folios = []
fechas = []    # formato dd/mm/aaaa hh:mm
estados = []   # Pendiente, Derivado o Archivado

TIPOS_PERMITIDOS = ["SOLICITUD", "OFICIO", "CARTA", "CONSTANCIA",
                    "MATRICULA", "MATRÍCULA", "CERTIFICADO", "RECLAMO"]

ARCHIVO = "expedientes.txt"
