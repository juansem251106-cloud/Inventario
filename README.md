URL github: https://github.com/juansem251106-cloud/Inventario.git

# Sistema de Inventario en Python

## Descripción

Este proyecto consiste en un sistema de inventario desarrollado en Python que permite gestionar productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), además de calcular estadísticas y manejar persistencia de datos utilizando archivos CSV.

El programa funciona a través de un menú en consola y utiliza una estructura modular para organizar el código.

---

## Estructura del Proyecto

inventario/

* app.py → Programa principal (menú e interacción con el usuario)
* servicios.py → Lógica del negocio (CRUD y estadísticas)
* archivos.py → Manejo de archivos CSV (guardar y cargar)

---

## Estructura de Datos

El inventario se almacena en memoria como una lista de diccionarios:

```python
{
    "nombre": "Producto",
    "precio": 10.5,
    "cantidad": 3
}
```

---

## Funcionalidades

### CRUD de productos

* Agregar productos
* Mostrar inventario
* Buscar productos por nombre
* Actualizar precio y/o cantidad
* Eliminar productos

### Estadísticas

* Total de unidades
* Valor total del inventario
* Producto más caro
* Producto con mayor stock

### Persistencia (CSV)

* Guardar inventario en archivo CSV
* Cargar inventario desde CSV
* Validación de formato y datos
* Opción de sobrescribir o fusionar datos

---

## Validaciones

El sistema incluye validaciones para:

* Opciones del menú (solo valores entre 1 y 9)
* Precio (número decimal no negativo)
* Cantidad (número entero no negativo)
* Formato del archivo CSV
* Manejo de errores en lectura/escritura de archivos

---

## Uso del Programa

1. Ejecutar el archivo principal:

```bash
python app.py
```

2. Seleccionar una opción del menú:

* 1 → Agregar producto
* 2 → Mostrar inventario
* 3 → Buscar producto
* 4 → Actualizar producto
* 5 → Eliminar producto
* 6 → Ver estadísticas
* 7 → Guardar CSV
* 8 → Cargar CSV
* 9 → Salir

---

## Manejo de Errores

El sistema está preparado para evitar fallos inesperados:

* Captura errores de entrada del usuario
* Evita que el programa se cierre por archivos inválidos
* Omite filas incorrectas al cargar CSV y reporta el número de errores

---

## Tecnologías Utilizadas

* Python 3
* Módulo csv (manejo de archivos)

---

## Autor

Proyecto desarrollado como práctica de programación en Python.
