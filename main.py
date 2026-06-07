# main.py
# Punto de entrada del programa
 
# --- Prueba del Día 2 ---
# from src.productos import
# productos = []

# p1 = crear_producto(1, "Leche", 1500.0, 10)
# p2 = crear_producto(2, "Pan", 800.0, 25)
# p3 = crear_producto(3, "Agua", 500.0, 50)

# productos.append(p1)
# productos.append(p2)
# productos.append(p3)

# imprimir_lista(productos)

# productos = agregar_producto(productos)
# imprimir_lista(productos)


# -- Prueba del Día 4 --

from src.productos import (
    crear_producto,
    agregar_producto,
    modificar_producto,
    eliminar_producto,
    imprimir_lista
)

# --- Datos de prueba ---

productos = []

productos.append(crear_producto(1, "Leche", 1500.0, 10.0))
productos.append(crear_producto(2, "Pan", 800.0, 25.0))
productos.append(crear_producto(3, "Agua", 500.0, 50.0))

# --- Prueba Modificar ---
productos = modificar_producto(productos)
imprimir_lista(productos)

# -- Prueba Eliminar ---
productos = eliminar_producto(productos)
imprimir_lista(productos)