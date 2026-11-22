# registro.py - Registro de nuevos expedientes.
from datetime import datetime
import datos
from validaciones import validarDNI, validarTipo, validarDatos
from archivos import guardarExpedientes


def generarCodigo(numero):
    """Arma el código EXP-2026-NNNN con ceros a la izquierda."""
    return "EXP-2026-" + str(numero).zfill(4)


def limpiar(texto):
    """Quita espacios sobrantes y cambia ';' por ',' (';' separa los campos del archivo)."""
    return texto.strip().replace(";", ",")


def registrarExpediente():
    # Repite hasta que todos los datos sean válidos.
    while True:
        dni = limpiar(input("Ingrese DNI: "))
        nombre = limpiar(input("Ingrese nombres y apellidos: "))
        tipo = limpiar(input("Tipo de documento: ")).upper()
        asunto = limpiar(input("Ingrese asunto: "))
        cantidad = limpiar(input("Cantidad de folios: "))

        if not validarDNI(dni):
            print("DNI inválido. Debe tener 8 dígitos. Intente de nuevo.\n")
        elif not validarTipo(tipo):
            print("Tipo de documento no permitido. Intente de nuevo.\n")
        elif not validarDatos(nombre, asunto, cantidad):
            print("Datos inválidos: complete todos los campos y use folios > 0. Intente de nuevo.\n")
        else:
            break

    codigo = generarCodigo(len(datos.codigos) + 1)
    datos.codigos.append(codigo)
    datos.dnis.append(dni)
    datos.nombres.append(nombre)
    datos.tipos.append(tipo)
    datos.asuntos.append(asunto)
    datos.folios.append(int(cantidad))
    datos.fechas.append(datetime.now().strftime("%d/%m/%Y %H:%M"))
    datos.estados.append("Pendiente")

    guardarExpedientes()
    print("\nExpediente registrado correctamente.")
    print("Cargo de recepción:", codigo, "-", datos.fechas[-1])
