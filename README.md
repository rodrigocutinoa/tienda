PYTHON PROYECTO TIENDA
======================


Estructura del proyecto
-----------------------

tienda/
│
├── .venv/               <-- Ignorado por Git
├── data/                <-- Carpeta para tus archivos JSON/CSV
│   └── inventario.json
│
├── src/                  <-- Código fuente (Source)
│   ├── __init__.py       <-- Indica que 'src' es un paquete
│   ├── productos.py      <-- Lógica de agregar, eliminar, editar
│   ├── ventas.py         <-- Lógica de pedidos y transacciones
│   └── persistencia.py   <-- Lógica de guardar/leer archivos
│
├── .gitignore            <-- Configurado (v. oficial GitHub)
├── main.py               <-- Punto de entrada (el menú principal)
├── README.md             <-- Explicación de tu proyecto
└── requirements.txt      <-- Tu manifiesto de dependencias





Semana 1: El Corazón del Sistema (Módulo productos.py)
------------------------------------------------------
En esta etapa, el objetivo es dominar la lógica y las validaciones. No te preocupes por guardar archivos todavía; usa una lista global en memoria.

    Día 1: Estructura de carpetas y main.py. Crea un menú que imprima "Hola" y salga.
    Día 2: productos.py: Define la estructura de datos (recomiendo una lista de diccionarios) y la función crear_producto con Type Hinting.
    Día 3: Validaciones. Asegúrate de que el precio sea float y positivo. Si falla, lanza un error o devuelve un mensaje claro.
    Día 4: Funciones leer y actualizar.
    Día 5: Función eliminar y búsqueda por ID.
    Día 6: Integración en main.py. Que el menú realmente llame a las funciones de productos.py.
    Día 7: Refactorización: Limpia tu código y asegúrate de que cada función haga una sola cosa (Principio de Responsabilidad Única).


Semana 2: Persistencia (Módulo persistencia.py)
-----------------------------------------------
Es mejor aprender a guardar datos ahora. Así, cuando pases a "Ventas", ya tendrás productos reales que cargar.

    Día 8: Introducción a JSON. Crea una función que tome una lista y la guarde en data/inventario.json.
    Día 9: Carga de datos. Al abrir el programa, main.py debe leer el JSON.
    Día 10: Manejo de errores de archivo: ¿Qué pasa si el archivo .json no existe? (Uso de try/except FileNotFoundError).
    Día 11: Robustez: Asegúrate de que, después de cada "Agregar" o "Eliminar", el archivo se actualice automáticamente.
    Día 12-14: Repaso y ajustes de bugs.


Semana 3: Transacciones (Módulo ventas.py)
------------------------------------------
Aquí es donde aplicas lógica de negocio más compleja.

    Día 15: Estructura de un "Pedido". Un pedido necesita un ID de cliente, una fecha y una lista de productos.
    Día 16: Lógica de stock. Al vender, debes restar la cantidad del inventario en productos.py.
    Día 17: Validación de stock: No puedes vender 10 cafés si solo tienes 5.
    Día 18: Cálculo de totales e impuestos.
    Día 19: Guardar historial de ventas en un nuevo archivo ventas.json.
    Día 20: Reporte simple: "Total vendido en el día".


-----------------------------------------------

Consejos de "Ingeniero a Ingeniero" para tu horario:
1. Deja el código "caliente": Cuando termines tus 30-60 minutos, deja un comentario que diga:
# SIGUIENTE PASO: Terminar la validación del ID. Esto evita que al día siguiente pierdas 15 minutos recordando qué estabas haciendo.

2. Modularidad Real (Separación de Conceptos):
    - productos.py no debe tener input() ni print(). Debe recibir datos y retornar datos o errores.
    - main.py es el único que habla con el usuario (tiene los input).
    - Esto se llama Separación de Concernimientos (SoC) y es lo que diferencia a un programador de un ingeniero.



Módulo	Responsabilidad
-----------------------
    - main.py	Interfaz de usuario (Menú, capturar datos).
    - productos.py	Reglas de negocio (¿Es válido el precio? ¿Existe el ID?).
    - persistencia.py	El "mensajero" (Solo lee y escribe en disco).


Si un día estás demasiado cansado para programar, dedica esos 30 minutos a escribir el README.md o a diseñar el flujo en un papel. El diseño también es programar.




GITHUB
------
Tip de Ingeniero: Adopta Conventional Commits. No uses mensajes como "cambios" o "arreglo". Usa prefijos:
    feat: (nueva funcionalidad)
    fix: (corregir un error)
    docs: (cambios en documentación)
    refactor: (mejorar código sin cambiar funcionalidad)




PASOS AIDCIONALES
=================


PYTHON
------
# 1. Borra el entorno virtual viejo (que tiene la versión vieja)
rm -rf .venv

# 2. Crea el nuevo entorno (usará la versión más nueva que instalaste)
python3 -m venv .venv

# 3. Instala tus librerías de nuevo (usando tu archivo de manifiesto)
pip install -r requirements.txt




gitignore
---------
.gitignore
Descomenta .vscode/ y .idea/ Haz que Git las ignore por completo.

Configura cada equipo por separado: La primera vez que bajes el código en la otra máquina, VS Code te preguntará: "He detectado un entorno virtual, ¿quieres usarlo?". Dile que sí en esa máquina. Eso creará una carpeta .vscode/ local en esa computadora que Git ignorará.



Archivo requirements.txt
------------------------
Usa un archivo requirements.txt: Como no vas a subir la carpeta .venv (que está en el .gitignore), esta es la forma profesional de mantener tus equipos sincronizados:

requirements.txt
# --- Formateo y Estilo (Calidad de Código) ---
black==25.1.0        # Mantiene tu código limpio y profesional automáticamente
# --- Interfaz de Usuario ---
tabulate==0.9.0      # Para imprimir el inventario en tablas elegantes en la terminal
# --- Utilidades ---
python-dateutil==2.9.0  # Útil para manejar fechas en el módulo de Ventas


Tip Pro: Para que ambos equipos tengan las mismas librerías, cada vez que instales algo, ejecuta en la terminal:
    pip freeze > requirements.txt

Al cambiar de equipo, solo ejecutas:
    pip install -r requirements.txt



Mac OS permisos para la Terminal y VSC
--------------------------------------
- Click en el Apple Menu () > System Settings.
- Ve a Privacy & Security.
- Busca y haz click en Full Disk Access.
- Busca Terminal y Visual Studio Code en la lista y asegúrate de que el interruptor esté en ON (azul).
- Si no aparecen en la lista, dale al botón + al final, ve a la carpeta "Applications" y agrégalos.
- IMPORTANTE: Te pedirá que cierres la aplicación para aplicar los cambios (Quit & Reopen). Hazlo.

Nota: Si no aparecen para agregar la aplicación
Terminal -> Se abrirá un buscador de archivos (Finder). Presiona Cmd + Shift + G y escribe /Applications/Utilities/
VSC -> Haz lo mismo para Visual Studio Code (este suele estar directamente en la carpeta /Applications/


Resetear los permisos de Git
A veces, macOS registra una versión específica de una app y, si se actualiza, el permiso se corrompe. Ejecuta esto en tu terminal
    tccutil reset All com.microsoft.VSCode
    tccutil reset All com.apple.Terminal

Usar el comando de "Propiedad"
Como ingeniero, te recomiendo asegurar que tu usuario es el dueño absoluto de esa carpeta dev. Ejecuta esto:
    sudo chown -R $(whoami) /Users/rodrigo/dev






EXTENCIONES RECOMENDADAS
------------------------

1. Python (de Microsoft)
Es la extensión obligatoria. No es solo una; es un paquete que incluye soporte para edición, depuración y navegación de código.

Para qué sirve: Te permite ejecutar el código con un clic, habilita el autocompletado (IntelliSense) y te permite hacer "Debug" (detener el programa en una línea para ver qué está pasando por dentro).

2. Pylance
Suele instalarse junto con la de Python, pero asegúrate de que esté activa.

Para qué sirve: Es el "cerebro" que analiza tu código mientras escribes. Te avisará si intentas usar una variable que no existe o si estás pasando un string donde definiste que iba un int (gracias al Type Hinting que mencionamos).

3. Black Formatter
En ingeniería, no perdemos tiempo alineando espacios a mano; dejamos que la máquina lo haga.

Para qué sirve: Cada vez que guardes el archivo (Ctrl + S), Black reordenará tu código para que cumpla estrictamente con el estándar PEP 8. Esto hace que tu código se vea profesional y uniforme, sin importar si lo escribiste en Mac o en Windows.

4. Error Lens
Esta es increíble para aprender.

Para qué sirve: En lugar de mostrarte una pequeña línea roja ondulada abajo de un error, escribe el error directamente al final de la línea de código en color rojo o amarillo. Te ayuda a ver las fallas de sintaxis al instante sin tener que poner el mouse encima.

5. GitLens — Git supercharged
Como vas a usar mucho GitHub, esta herramienta es tu mejor aliada.

Para qué sirve: Te muestra quién, cuándo y en qué commit se cambió cada línea de código. Si algo que funcionaba ayer hoy no funciona, GitLens te permite comparar las versiones rápidamente desde el editor.

6. Prettier (para archivos no-Python)
Para qué sirve: Ideal para mantener ordenados tus archivos README.md, archivos .json de datos y el propio .gitignore.