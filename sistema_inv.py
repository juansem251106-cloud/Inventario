from servicios import *
from archivos import *

inventario = []


def menu():
    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")


# -------- VALIDACIONES --------

def pedir_opcion():
    op = input("Opción (1-9): ")
    while not (op.isdigit() and 1 <= int(op) <= 9):
        print("Opción inválida")
        op = input("Opción (1-9): ")
    return op


def pedir_precio(msg):
    dato = input(msg)
    while not dato.replace(".", "", 1).isdigit():
        print("Debe ser un número")
        dato = input(msg)

    valor = float(dato)
    while valor < 0:
        print("No puede ser negativo")
        dato = input(msg)
        if dato.replace(".", "", 1).isdigit():
            valor = float(dato)
    return valor


def pedir_cantidad(msg):
    dato = input(msg)
    while not dato.isdigit():
        print("Debe ser un número entero")
        dato = input(msg)

    valor = int(dato)
    return valor


# -------- PROGRAMA PRINCIPAL --------

opcion = ""

while opcion != "9":
    menu()
    opcion = pedir_opcion()

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = pedir_precio("Precio: ")
        cantidad = pedir_cantidad("Cantidad: ")
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Buscar: ")
        res = buscar_producto(inventario, nombre)
        print(res if res else "Producto no encontrado")

    elif opcion == "4":
        nombre = input("Producto a actualizar: ")

        p = input("Nuevo precio (enter omitir): ")
        c = input("Nueva cantidad (enter omitir): ")

        nuevo_precio = None
        nueva_cantidad = None

        if p:
            if p.replace(".", "", 1).isdigit():
                valor = float(p)
                if valor >= 0:
                    nuevo_precio = valor
                else:
                    print("Precio inválido")
            else:
                print("Precio inválido")

        if c:
            if c.isdigit():
                nueva_cantidad = int(c)
            else:
                print("Cantidad inválida")

        if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
            print("Producto actualizado")
        else:
            print("Producto no encontrado")

    elif opcion == "5":
        nombre = input("Producto a eliminar: ")
        if eliminar_producto(inventario, nombre):
            print("Eliminado")
        else:
            print("No encontrado")

    elif opcion == "6":
        stats = calcular_estadisticas(inventario)
        if stats:
            print("Unidades:", stats["unidades_totales"])
            print("Valor total:", stats["valor_total"])
            print("Más caro:", stats["producto_mas_caro"])
            print("Mayor stock:", stats["producto_mayor_stock"])
        else:
            print("Inventario vacío")

    elif opcion == "7":
        ruta = input("Nombre del archivo: ")
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("Archivo a cargar: ")
        nuevos = cargar_csv(ruta)

        if nuevos:
            decision = input("¿Sobrescribir inventario? (S/N): ").lower()

            if decision == "s":
                inventario = nuevos
            else:
                # fusionar por nombre
                for nuevo in nuevos:
                    existente = buscar_producto(inventario, nuevo["nombre"])
                    if existente:
                        existente["cantidad"] += nuevo["cantidad"]
                    else:
                        inventario.append(nuevo)

    elif opcion == "9":
        print("Programa finalizado")

    else:
        print("Opción inválida")