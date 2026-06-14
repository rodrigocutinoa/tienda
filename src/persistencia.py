# src/persistencia.py
# Responsabilidad: Guardar y cargar datos en archivos

import json  # librería estándar de Python para manejar JSON
import os    # librería para manejar rutas y archivos del sistema


# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

# Ruta del archivo donde se guardarán los productos
# os.path.join construye la ruta correcta en cualquier sistema operativo

RUTA_PRODUCTOS = os.path.join("data", "productos.json")


# --------------------------------------------------
# GUARDAR PRODUCTOS
# --------------------------------------------------

def guardar_productos(productos):
    """
    Guarda la lista de productos en un archivo JSON.

    Parámetros:
        productos (list): Lista de productos a guardar

    Retorna:
        bool: True si guardó correctamente, False si hubo error
    """
    try:
        # Abre el archivo en modo escritura ("w")
        # Si el archivo no existe, lo crea automáticamente
        # encoding="utf-8" para soportar caracteres especiales (tildes, ñ)
        with open(RUTA_PRODUCTOS, "w", encoding="utf-8") as archivo:
            # Convierte la lista a formato JSON y la escribe en el archivo
            # indent=4 hace el archivo legible con sangría de 4 espacios
            # ensure_ascii=False permite guardar tildes y ñ correctamente
            json.dump(productos, archivo, indent=4, ensure_ascii=False)

        print(f"  ✅ Productos guardados correctamente.")
        return True

    except Exception as error:
        # Si algo falla, muestra el error sin romper el programa
        print(f"  ❌ Error al guardar productos: {error}")
        return False


# --------------------------------------------------
# CARGAR PRODUCTOS
# --------------------------------------------------

def cargar_productos():
    """
    Carga la lista de productos desde el archivo JSON.

    Retorna:
        list: Lista de productos cargados,
              lista vacía si el archivo no existe o hay error
    """
    try:
        # Verifica si el archivo existe antes de abrirlo
        # Evita el error si es la primera vez que se ejecuta el programa
        if not os.path.exists(RUTA_PRODUCTOS):
            print(" ℹ️  No se encontró archivo de productos.")
            print(" ℹ️  Iniciando con lista vacía.")
            return []
        
        # Abre el archivo en modo lectura ("r")
        with open(RUTA_PRODUCTOS, "r", encoding="utf-8") as archivo:

            # Convierte el JSON del archivo a lista de diccionarios
            productos = json.load(archivo)

        print(f"  ✅ {len(productos)} Producto(s) cargado(s) correctamente")
        return productos
    
    except Exception as error:
        # Si algo falla, inicia con lista vacía sin romper el programa
        print(f"  ❌ Error al cargar productos: {error}")
        return []