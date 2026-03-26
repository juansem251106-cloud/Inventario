
def pedir_opcion():
    op = input("Opción (1-9): ")
    while not (op.isdigit() and 1 <= int(op) <= 9):
        print("\n(!) Opción inválida\n")
        op = input("Opción (1-9): ")
    return op


def pedir_precio(msg):
    dato = input(msg)
    while not dato.replace(".", "", 1).isdigit():
        print("\n(!) Ingrese un valor valido\n")
        dato = input(msg)

    valor = float(dato)
    while valor < 0:
        print("\n(!) No puede ser negativo\n")
        dato = input(msg)
        if dato.replace(".", "", 1).isdigit():
            valor = float(dato)
    return valor


def pedir_cantidad(msg):
    dato = input(msg)
    while not dato.isdigit():
        print("\n(!) Debe ser un numero entero\n")
        dato = input(msg)

    valor = int(dato)
    return valor

def agregar_producto(inv, nombre, precio, cantidad):
    inv.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inv):
    if not inv:
        print("\n(!) Inventario vacío\n")
        return

    for p in inv:
        print(f"\n{p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inv, nombre):
    for p in inv:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inv, nombre, nuevo_precio=None, nueva_cantidad=None):
    prod = buscar_producto(inv, nombre)
    if prod:
        if nuevo_precio is not None:
            prod["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            prod["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inv, nombre):
    prod = buscar_producto(inv, nombre)
    if prod:
        inv.remove(prod)
        return True
    return False


def calcular_estadisticas(inv):
    if not inv:
        return None

    unidades_totales = sum(p["cantidad"] for p in inv)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inv)

    producto_mas_caro = max(inv, key=lambda p: p["precio"])
    producto_mayor_stock = max(inv, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }