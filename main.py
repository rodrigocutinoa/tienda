# main.py
# Punto de entrada del programa
 
from src.productos import crear_producto, imprimir_lista, agregar_producto

# --- Prueba del Día 2 ---
productos = []

# p1 = crear_producto(1, "Leche", 1500.0, 10)
# p2 = crear_producto(2, "Pan", 800.0, 25)
# p3 = crear_producto(3, "Agua", 500.0, 50)

# productos.append(p1)
# productos.append(p2)
# productos.append(p3)

# imprimir_lista(productos)

productos = agregar_producto(productos)
imprimir_lista(productos)