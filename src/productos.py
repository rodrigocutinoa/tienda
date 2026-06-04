# src/productos.py
# Responsabilidad: Lógica de gestión de productos


# --------------------------------------------------
# MODELO DE DATOS
# --------------------------------------------------

def crear_producto(id, nombre, precio, cantidad):
    """
    Crea y retorna un producto como diccionario.

    Parámetros:
        id       (int)   : Identificador único
        nombre   (str)   : Nombre del producto
        precio   (float) : Precio del producto
        cantidad (int)   : Stock disponible

    Retorna:
        dict: Producto con sus atributos
    """
    return {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }


# --------------------------------------------------
# MOSTRAR PRODUCTOS
# --------------------------------------------------

def imprimir_producto(producto):
    """Imprime un producto formateado en pantalla"""
    print(f"  ID       : {producto['id']}")
    print(f"  Nombre  : {producto['nombre']}")
    print(f"  Precio   : ${producto['precio']:.2f}")
    print(f"  Cantidad  : {producto['cantidad']}")
    print(f" {'-' * 30}")


def imprimir_lista(productos):
    """Imprime todos los productos de la lista."""
    if not productos:
        print("No hay productos registrados")
        return
    
    print(f"\n {'-' * 30}")
    print(f"  LISTA DE PRODUCTOS")
    print(f" {'-' * 30}\n")

    for producto in productos:
        imprimir_producto(producto)