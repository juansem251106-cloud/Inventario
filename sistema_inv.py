from servicios import *
from archivos import *

inventario = []


def menu():
    print("\n\===( MENU )===/")
    print("-"*19)
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir\n")
    print("-"*19)

# -------- PROGRAMA PRINCIPAL --------

opcion = ""

while opcion != "9":
    menu()
    opcion = pedir_opcion()

    if opcion == "1":
        nombre = input("Nombre: ").capitalize()
        precio = pedir_precio("Precio: ")
        cantidad = pedir_cantidad("Cantidad: ")
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Buscar: ")
        res = buscar_producto(inventario, nombre)
        print(res if res else "\n(!) Producto no encontrado\n")

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
                    print("\n(!) Precio inválido\n")
            else:
                print("\n(!) Precio inválido\n")

        if c:
            if c.isdigit():
                nueva_cantidad = int(c)
            else:
                print("\n(!) Cantidad inválida\n")

        if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
            print("Producto actualizado")
        else:
            print("\n(!) Producto no encontrado\n")

    elif opcion == "5":
        nombre = input("Producto a eliminar: ")
        if eliminar_producto(inventario, nombre):
            print("Eliminado")
        else:
            print("\n(!) No encontrado\n")

    elif opcion == "6":
        stats = calcular_estadisticas(inventario)
        if stats:
            print("Unidades:", stats["unidades_totales"])
            print("Valor total:", stats["valor_total"])
            print("Más caro:", stats["producto_mas_caro"])
            print("Mayor stock:", stats["producto_mayor_stock"])
        else:
            print("\n(!) Inventario vacío\n")

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
                for nuevo in nuevos:
                    existente = buscar_producto(inventario, nuevo["nombre"])
                    if existente:
                        existente["cantidad"] += nuevo["cantidad"]
                    else:
                        inventario.append(nuevo)

    elif opcion == "9":
        print("\nPrograma finalizado\n")

    else:
        print("\n(!) Opción inválida\n")