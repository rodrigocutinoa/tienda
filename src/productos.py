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
    print(f"  ID        : {producto['id']}")
    print(f"  Nombre    : {producto['nombre']}")
    print(f"  Precio    : ${producto['precio']:.2f}")
    print(f"  Cantidad  : {producto['cantidad']:.1f}")
    print(f"  {'-' * 30}")


def imprimir_lista(productos):
    """Imprime todos los productos de la lista."""
    if not productos:
        print("  No hay productos registrados")
        return
    
    print(f"\n  {'-' * 30}")
    print(f"  LISTA DE PRODUCTOS")
    print(f"  {'-' * 30}\n")

    for producto in productos:
        imprimir_producto(producto)


# --------------------------------------------------
# VALIDACIONES
# --------------------------------------------------

def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío.

    Parámetros:
        nombre (str): Nombre a validar

    Retorna:
        bool: True si es válido, False si no
    """
    return len(nombre.strip()) > 0


def validar_precio(precio):
    """
    Valida que el precio sea un número mayor a cero.

    Parámetros:
        precio (float): Precio a validar

    Retorna:
        bool: True si es válido, False si no
    """
    return precio > 0


def validar_cantidad(cantidad):
    """
    Valida que la cantidad sea un número entero mayor o igual a cero.

    Parámetros:
        cantidad (int): Cantidad a validar

    Retorna:
        bool: True si es válido, False si no
    """
    return cantidad >= 0


# --------------------------------------------------
# AGREGAR PRODUCTO
# --------------------------------------------------

def agregar_producto(productos):
    """
    Solicita datos al usuario y agrega un producto a la lista.

    Parámetros:
        productos (list): Lista actual de productos

    Retorna:
        list: Lista actualizada con el nuevo producto
    """
    print(f"\n {'-' * 30}")
    print("  AGREGAR NUEVO PRODUCTO")
    print(f"  {'-' * 30}\n")

    # -- Nombre --
    nombre = input("  Nombre del producto: ").strip()
    if not validar_nombre(nombre):
        print("  ❌ El nombre no puede estar vacío.")
        return productos
    
    
    # -- Precio --
    try:
        precio = float(input("  Precio: "))
        if not validar_precio(precio):
            print("  ❌ El precio debe ser mayor a cero.")
            return productos
    except ValueError:
        print("  ❌ El precio debe ser un número.")
        return productos


    # -- Cantidad --
    try:
        cantidad = float(input("  Cantidad: "))
        if not validar_cantidad(cantidad):
            print("  ❌ La cantidad no puede ser negativa.")
            return productos
    except ValueError:
        print("  ❌ La cantidad debe ser un número entero.")
        return productos
    

    # --- Crear y agregar ---
    id_nuevo = len(productos) + 1 # ID secuencial
    producto = crear_producto(id_nuevo, nombre, precio, cantidad)
    productos.append(producto)

    print(f"  ✅ Producto {producto} agregado con ID {id_nuevo}.")
    return productos
    


# --------------------------------------------------
# BUSCAR PRODUCTO
# --------------------------------------------------

def buscar_producto(productos, id):
    """
    Busca un producto por ID en la lista.

    Parámetros:
        productos (list): Lista de productos
        id        (int) : ID del producto a buscar

    Retorna:
        dict: Producto encontrado o None si no existe
    """
    for producto in productos:
        if producto["id"] == id:
            return producto
    return None


# --------------------------------------------------
# MODIFICAR PRODUCTO
# --------------------------------------------------

def modificar_producto(productos):
    """
    Solicita un ID y modifica los datos del producto encontrado.

    Parámetros:
        productos (list): Lista actual de productos

    Retorna:
        list: Lista actualizada con el producto modificado
    """
    print(f"\n  {'-' * 30}")
    print("  MODIFICAR PRODUCTOS")
    print(f"  {'-' * 30} \n")

    # imprimir_lista(productos)

    try:
        id = int(input("  ID del producto a modificar: "))
    except ValueError:
        print("  ❌ El ID debe ser un número entero.")
        return productos

    producto = buscar_producto(productos, id)
    if productos is None:
        print(f"  ❌ No se encontró un producto con ID {id}.")
        return productos


    print(f"  Producto encontrado:")
    imprimir_producto(producto)


# -- Nuevo nombre --
    nombre = input("  Nuevo nombre del producto: ").strip()
    if nombre and validar_nombre(nombre):
        producto['nombre'] = nombre


# -- Nuevo precio --
    precio_input = input("  Nuevo precio (Enter para mantener): ").strip()
    if precio_input:
        try:
            precio = float(precio_input)
            if validar_precio(precio):
                producto['precio'] = precio
            else:
                print('  ⚠️ Precio inválido, se mantiene el anterior')
        except ValueError:
            print(' ⚠️ Precio inválido, se mantiene el anterior.')


# -- Nueva cantidad --
    cantidad_input = input("  Nueva cantidad (Enter para mantener: ").strip()
    if cantidad_input:
        try:
            cantidad = float(cantidad_input)
            if validar_cantidad(cantidad):
                producto['cantidad'] = cantidad
            else:
                print(f" ⚠️ Cantidad inválida, se mantiene la anterior.")
        except ValueError:
            print("  ⚠️ Cantidad inválida, se mantiene la anterior.")

    print(f"\n  ✅ Producto con ID {id} modificado correctamente.")
    return productos


# --------------------------------------------------
# ELIMINAR PRODUCTO
# --------------------------------------------------

def eliminar_producto(productos):
    """
    Solicita un ID y elimina el producto correspondiente.

    Parámetros:
        productos (list): Lista actual de productos

    Retorna:
        list: Lista actualizada sin el producto eliminado
    """
    print(f"\n  {'-' * 30}")
    print("  ELIMINAR PRODUCTO")
    print(f"  {'-' * 30 }\n")

    try:
        id = int(input("  ID del producto a eliminar: "))
    except ValueError:
        print("  ❌ El ID debe ser un número entero.")
        return productos

    producto = buscar_producto(productos, id)

    if producto is None:
        print(f"  ❌ No existe un producto con ID {id}.")
        return productos

    print(f"  Producto encontrado")
    imprimir_producto(producto)

    confirmacion = input(f"  ¿Confirma eliminar? (s/n): ").strip().lower()
    if confirmacion == "s":
        productos.remove(producto)
        print(f"  ✅ Producto con ID {id} eliminado correctamente.")
    else:
        print(f"  ⚠️ Operación cancelada.")
        return productos

    