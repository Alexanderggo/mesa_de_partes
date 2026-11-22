# main.py - Menú principal del prototipo de Mesa de Partes Digital.
import datos
from archivos import cargarExpedientes, guardarExpedientes
from registro import registrarExpediente
from busqueda import buscarExpediente
from ordenamiento import ordenarExpedientes


def mostrarMenu():
    print("\n===== MESA DE PARTES DIGITAL =====")
    print("1. Registrar expediente")
    print("2. Buscar expediente por código")
    print("3. Ordenar y listar expedientes")
    print("4. Guardar y salir")


def mostrarExpediente(i):
    print()
    print("Código:".ljust(13), datos.codigos[i])
    print("DNI:".ljust(13), datos.dnis[i])
    print("Solicitante:".ljust(13), datos.nombres[i])
    print("Documento:".ljust(13), datos.tipos[i])
    print("Asunto:".ljust(13), datos.asuntos[i])
    print("Folios:".ljust(13), datos.folios[i])
    print("Recepción:".ljust(13), datos.fechas[i])
    print("Estado:".ljust(13), datos.estados[i])


def listarExpedientes():
    if len(datos.codigos) == 0:
        print("No hay expedientes registrados.")
    else:
        for i in range(len(datos.codigos)):
            print(datos.codigos[i], "|", datos.fechas[i], "|", datos.nombres[i],
                  "|", datos.tipos[i], "|", datos.estados[i])


def main():
    cargarExpedientes()
    opcion = ""
    while opcion != "4":
        mostrarMenu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrarExpediente()
        elif opcion == "2":
            codigo = input("Ingrese código: ").strip().upper()
            i = buscarExpediente(codigo)
            if i == -1:
                print("El expediente no existe.")
            else:
                mostrarExpediente(i)
        elif opcion == "3":
            criterio = input("Ordenar por (1) fecha o (2) código: ").strip()
            if criterio == "1":
                ordenarExpedientes("fecha")
            elif criterio == "2":
                ordenarExpedientes("codigo")
            else:
                print("Criterio inválido.")
                continue
            listarExpedientes()
        elif opcion == "4":
            guardarExpedientes()
            print("Cerrando sistema...")
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
