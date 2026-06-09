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

# from src.productos import (
#     crear_producto,
#     agregar_producto,
#     modificar_producto,
#     eliminar_producto,
#     imprimir_lista
# )

# # --- Datos de prueba ---

# # Lista de productos en memoria
# productos = []

# # --- Datos de prueba ---
# productos.append(crear_producto(1, "Leche", 1500.0, 10.0))
# productos.append(crear_producto(2, "Pan", 800.0, 25.0))
# productos.append(crear_producto(3, "Agua", 500.0, 50.0))

# # -- Imprimri lista antes de modificar --
# print(f"\n  == LISTA INICIAL ==")
# imprimir_lista(productos)

# # --- Prueba Modificar ---
# productos = modificar_producto(productos)
# print("\n  === LISTA DESPUÉS DE MODIFICAR ===")
# imprimir_lista(productos)

# # -- Prueba Eliminar ---
# productos = eliminar_producto(productos)
# print("\n  === LISTA DESPUÉS DE ELIMINAR ===")
# imprimir_lista(productos)


# ----------------------------------------------------------

from src.productos import (
    agregar_producto,
    modificar_producto,
    eliminar_producto,
    imprimir_lista
)

from src.persistencia import guardar_productos


# --------------------------------------------------
# MENÚ
# --------------------------------------------------

def mostrar_menu():
    """Imprime las opciones del menú principal."""
    print(f"\n  {'-' * 30}")
    print(f"  TIENDA — MENÚ PRINCIPAL")
    print(f"  {'-' * 30}\n")
    print(f"  1. Ver productos")
    print(f"  2. Agregar producto")
    print(f"  3. Modificar producto")
    print(f"  4. Eliminar producto")
    print(f"  5. Guardar productos")
    print(f"  0. Salir")
    print(f"  {'=' * 30}")


def ejecutar_opcion(opcion, productos):
    """
    Ejecuta la función correspondiente a la opción elegida.

    Parámetros:
        opcion   (str) : Opción elegida por el usuario
        productos (list): Lista actual de productos

    Retorna:
        list: Lista de productos actualizada
    """
    if opcion == "1":
        imprimir_lista(productos)

    elif opcion == "2":
        productos = agregar_producto(productos)

    elif opcion == "3":
        productos = modificar_producto(productos)

    elif opcion == "4":
        productos = eliminar_producto(productos)

    elif opcion == "5":
        productos = guardar_productos(productos)

    elif opcion == "0":
        print("\n  👋 Hasta luego!\n")

    else:
        print("\n  ❌ Opción inválida. Intente nuevamente")
    
    return productos


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

def main():
    """Función principal — inicia el programa."""
    productos = []
    
    while True:
        mostrar_menu()
        opcion = input("\n  Seleccione una opción: "). strip()
        productos = ejecutar_opcion(opcion, productos)

        if opcion == "0":
            break


# --------------------------------------------------
# PUNTO DE ENTRADA
# --------------------------------------------------

if __name__ == "__main__":
    main()