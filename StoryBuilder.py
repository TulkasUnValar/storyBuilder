"""
Juego educativo: El constructor de historias
- Objetivo: lectura, comprensión y creatividad para niños/as de 7–10 años.
- Incluye:
  * Versión en consola (con while, if/elif/else, for).
  * Versión gráfica sencilla con Tkinter (texto + imagen + botones).
"""

# =========================
# 1. IMPORTACIONES
# =========================

import tkinter as tk  # Tkinter para la versión gráfica
from pathlib import Path  # Para manejar rutas de forma segura

# Carpeta base del proyecto (donde está este archivo .py)
BASE_DIR = Path(__file__).resolve().parent

# Carpeta donde están las imágenes: BASE_DIR / "img"
IMG_DIR = BASE_DIR / "img"

# Tamaño máximo deseado para mostrar las imágenes en Tkinter
MAX_IMG_WIDTH = 400    # ancho máximo en píxeles
MAX_IMG_HEIGHT = 300   # alto máximo en píxeles

# =========================
# 2. ESTRUCTURA DE LA HISTORIA
# =========================

# Diccionario que contiene los "nodos" de la historia.
# Cada clave es un id de nodo (string), y cada valor es otro dict con:
# - "texto": frase que se muestra.
# - "imagen": nombre del archivo de imagen.
# - "opciones": lista de opciones. Cada opción es un dict con:
#       - "texto": texto del botón / opción.
#       - "siguiente": id del nodo siguiente.
#
# EJEMPLO de imágenes que deberías crear y guardar en la misma carpeta:
#   - gato_corriendo.png
#   - gato_caja.png
#   - gato_espacio.png
#   - gato_carro.png
#   - gato_durmiendo.png
#   - gato_fiesta.png
#   - gato_cohete.png

HISTORIA = {
    "inicio": {
        "texto": "El gato corre.",
        "imagen": "gato_corriendo.png",
        "opciones": [
            {"texto": "Se esconde en una caja.", "siguiente": "caja"},
            {"texto": "Vuela al espacio.", "siguiente": "espacio"},
            {"texto": "Conduce un carro.", "siguiente": "carro"}
        ]
    },
    "caja": {
        "texto": "El gato se esconde en una caja misteriosa.",
        "imagen": "gato_caja.png",
        "opciones": [
            {"texto": "La caja está llena de juguetes.", "siguiente": "juguetes"},
            {"texto": "La caja es una puerta mágica.", "siguiente": "puerta_magica"},
            {"texto": "La caja solo es una caja. Se duerme.", "siguiente": "final_dormido"}
        ]
    },
    "espacio": {
        "texto": "El gato se pone un casco y vuela al espacio.",
        "imagen": "gato_espacio.png",
        "opciones": [
            {"texto": "Visita la luna de queso.", "siguiente": "luna_queso"},
            {"texto": "Se encuentra con gatos astronautas.", "siguiente": "gatos_astro"},
            {"texto": "Se queda flotando y mirando las estrellas.", "siguiente": "final_estrellas"}
        ]
    },
    "carro": {
        "texto": "El gato conduce un carro rojo muy rápido.",
        "imagen": "gato_carro.png",
        "opciones": [
            {"texto": "Va al parque a jugar.", "siguiente": "parque"},
            {"texto": "Va a una fiesta de gatos.", "siguiente": "fiesta"},
            {"texto": "Se pierde en la ciudad.", "siguiente": "final_ciudad"}
        ]
    },
    # Algunos posibles finales y continuaciones:
    "juguetes": {
        "texto": "Dentro de la caja hay pelotas, ratones de juguete y plumas.",
        "imagen": "gato_juguetes.png",
        "opciones": [
            {"texto": "Juega hasta cansarse y luego duerme feliz.", "siguiente": "final_dormido"},
            {"texto": "Comparte sus juguetes con otros gatos.", "siguiente": "final_amigos"},
            {"texto": "Construye una torre de juguetes.", "siguiente": "final_torre"}
        ]
    },
    "puerta_magica": {
        "texto": "La caja es una puerta mágica a un mundo de gatos gigantes.",
        "imagen": "gato_puerta_magica.png",
        "opciones": [
            {"texto": "Explora el nuevo mundo.", "siguiente": "final_explorar"},
            {"texto": "Regresa a casa porque extraña su cama.", "siguiente": "final_dormido"},
            {"texto": "Invita a sus amigos a ver el mundo mágico.", "siguiente": "final_amigos"}
        ]
    },
    "luna_queso": {
        "texto": "La luna es de queso y el gato la prueba con curiosidad.",
        "imagen": "gato_luna_queso.png",
        "opciones": [
            {"texto": "Comparte el queso con ratones espaciales.", "siguiente": "final_amigos"},
            {"texto": "Guarda un pedazo de queso para llevar a casa.", "siguiente": "final_estrellas"},
            {"texto": "Se hace famoso como el primer gato en comer luna.", "siguiente": "final_famoso"}
        ]
    },
    "gatos_astro": {
        "texto": "Los gatos astronautas lo invitan a su nave espacial.",
        "imagen": "gato_cohete.png",
        "opciones": [
            {"texto": "Viaja con ellos a Marte.", "siguiente": "final_explorar"},
            {"texto": "Juegan a flotar sin gravedad.", "siguiente": "final_estrellas"},
            {"texto": "Les enseña juegos de su casa.", "siguiente": "final_amigos"}
        ]
    },
    "parque": {
        "texto": "En el parque, el gato corre entre los árboles y las flores.",
        "imagen": "gato_parque.png",
        "opciones": [
            {"texto": "Conoce un perro amistoso.", "siguiente": "final_amigos"},
            {"texto": "Se sube a un árbol y mira todo desde arriba.", "siguiente": "final_explorar"},
            {"texto": "Se cansa y duerme bajo una sombra.", "siguiente": "final_dormido"}
        ]
    },
    "fiesta": {
        "texto": "En la fiesta, todos los gatos bailan y maúllan canciones.",
        "imagen": "gato_fiesta.png",
        "opciones": [
            {"texto": "Baila toda la noche.", "siguiente": "final_fiesta"},
            {"texto": "Come pastel de pescado.", "siguiente": "final_feliz"},
            {"texto": "Organiza un concurso de maullidos.", "siguiente": "final_famoso"}
        ]
    },
    # Nodos finales: sin opciones
    "final_dormido": {
        "texto": "El gato se acurruca y se queda profundamente dormido. Fin de la historia.",
        "imagen": "gato_durmiendo.png",
        "opciones": []
    },
    "final_amigos": {
        "texto": "El gato hace muchos amigos y juegan felices. Fin de la historia.",
        "imagen": "gato_amigos.png",
        "opciones": []
    },
    "final_torre": {
        "texto": "La torre de juguetes se cae, y el gato se ríe. Fin de la historia.",
        "imagen": "gato_juguetes.png",
        "opciones": []
    },
    "final_explorar": {
        "texto": "El gato explora lugares nuevos y descubre maravillas. Fin de la historia.",
        "imagen": "gato_explorar.png",
        "opciones": []
    },
    "final_estrellas": {
        "texto": "El gato mira las estrellas y sueña con más aventuras. Fin de la historia.",
        "imagen": "gato_estrellas.png",
        "opciones": []
    },
    "final_ciudad": {
        "texto": "Se pierde un rato, pero encuentra el camino de regreso. Fin de la historia.",
        "imagen": "gato_ciudad.png",
        "opciones": []
    },
    "final_famoso": {
        "texto": "El gato se vuelve famoso en todo el mundo. Fin de la historia.",
        "imagen": "gato_famoso.png",
        "opciones": []
    },
    "final_fiesta": {
        "texto": "La fiesta termina y todos aplauden al gato bailarín. Fin de la historia.",
        "imagen": "gato_fiesta.png",
        "opciones": []
    },
    "final_feliz": {
        "texto": "Con pastel de pescado y amigos, el gato es muy feliz. Fin de la historia.",
        "imagen": "gato_feliz.png",
        "opciones": []
    }
}


# =========================
# 3. VERSIÓN EN CONSOLA
# =========================

def mostrar_opciones_consola(opciones):
    """
    Muestra las opciones numeradas en consola.
    Usa un ciclo for para recorrer la lista de opciones.
    """
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion['texto']}")


def obtener_eleccion_consola(num_opciones):
    """
    Pide al usuario que elija un número entre 1 y num_opciones.
    Usa un while para validar la entrada.
    """
    while True:
        respuesta = input("Elige una opción (1, 2 o 3): ")
        if respuesta.isdigit():
            numero = int(respuesta)
            if 1 <= numero <= num_opciones:
                return numero
        print("Por favor, elige un número válido.")


def jugar_consola():
    """
    Bucle principal de la versión en consola.
    Usa while para avanzar por la historia hasta un nodo final.
    """
    print("=== El Constructor de Historias (Consola) ===")
    nodo_actual_id = "inicio"
    historia_completa = []  # lista de frases elegidas

    while True:
        nodo = HISTORIA[nodo_actual_id]
        texto = nodo["texto"]
        opciones = nodo["opciones"]

        print("\n" + texto)
        historia_completa.append(texto)

        if not opciones:
            # Nodo final (no hay opciones)
            print("\n¡Has llegado al final de esta historia!")
            break

        mostrar_opciones_consola(opciones)
        eleccion = obtener_eleccion_consola(len(opciones))
        nodo_actual_id = opciones[eleccion - 1]["siguiente"]

    # Mostrar la historia completa al final usando un for
    print("\n=== Historia completa ===")
    for linea in historia_completa:
        print("-", linea)


# =========================
# 4. VERSIÓN GRÁFICA CON TKINTER
# =========================

# Variables globales sencillas para la versión gráfica:
root = None
label_texto = None
label_imagen = None
botones = []
nodo_actual_id = "inicio"
historia_completa_gui = []
imagenes_cache = {}  # para no perder referencias a PhotoImage


def mostrar_imagen(nombre_archivo):
    """
    Carga y muestra una imagen en el label_imagen.

    Busca siempre los archivos dentro de la carpeta IMG_DIR
    y los redimensiona para que no superen MAX_IMG_WIDTH x MAX_IMG_HEIGHT.
    """
    if not nombre_archivo:
        label_imagen.config(image="", text="[Sin imagen]")
        return

    # Construimos la ruta completa a la imagen
    ruta_imagen = IMG_DIR / nombre_archivo

    # Si el archivo no existe, mostramos un mensaje y salimos
    if not ruta_imagen.exists():
        label_imagen.config(
            image="",
            text=f"[No se encontró {ruta_imagen.name}]"
        )
        return

    # Usamos un caché para no recargar la imagen cada vez
    if ruta_imagen not in imagenes_cache:
        # Carga de la imagen original
        img_original = tk.PhotoImage(file=str(ruta_imagen))

        # Obtenemos ancho y alto originales
        w = img_original.width()
        h = img_original.height()

        # Calculamos factores de reducción enteros
        factor_w = max(w // MAX_IMG_WIDTH, 1)
        factor_h = max(h // MAX_IMG_HEIGHT, 1)

        # Elegimos el factor más grande para que quepa en ambos ejes
        factor = max(factor_w, factor_h)

        if factor > 1:
            # subsample usa factores enteros: 2 = mitad, 3 = un tercio, etc.
            img_redimensionada = img_original.subsample(factor, factor)
        else:
            img_redimensionada = img_original

        imagenes_cache[ruta_imagen] = img_redimensionada

    img = imagenes_cache[ruta_imagen]
    label_imagen.config(image=img, text="")
    label_imagen.image = img  # mantener referencia


def mostrar_nodo_gui():
    """
    Actualiza el texto, la imagen y las opciones en la interfaz gráfica.
    """
    global nodo_actual_id, historia_completa_gui

    nodo = HISTORIA[nodo_actual_id]
    texto = nodo["texto"]
    opciones = nodo["opciones"]

    # Guardamos la frase en la historia completa
    historia_completa_gui.append(texto)

    # Actualizamos el texto
    label_texto.config(text=texto)

    # Actualizamos la imagen
    mostrar_imagen(nodo["imagen"])

    # Actualizamos botones de opciones
    # Primero, desactivamos todos
    for boton in botones:
        boton.config(text="", state="disabled", command=lambda: None)

    # Luego, configuramos según las opciones disponibles
    for i, opcion in enumerate(opciones):
        if i < len(botones):
            botones[i].config(
                text=opcion["texto"],
                state="normal",
                command=lambda idx=i: manejar_eleccion_gui(idx)
            )

    # Si no hay opciones, mostramos mensaje final
    if not opciones:
        label_texto.config(text=texto + "\n\n(Has llegado al final de la historia.)")


def manejar_eleccion_gui(indice_opcion):
    """
    Maneja la elección del usuario en la versión gráfica.
    Cambia al siguiente nodo y llama a mostrar_nodo_gui().
    """
    global nodo_actual_id
    nodo = HISTORIA[nodo_actual_id]
    opciones = nodo["opciones"]

    if 0 <= indice_opcion < len(opciones):
        nodo_actual_id = opciones[indice_opcion]["siguiente"]
        mostrar_nodo_gui()


def iniciar_gui():
    """
    Crea la ventana de Tkinter y muestra el primer nodo.
    """
    global root, label_texto, label_imagen, botones, nodo_actual_id, historia_completa_gui

    root = tk.Tk()
    root.title("El Constructor de Historias")

    # Marco principal
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    # Label de texto de historia
    label_texto = tk.Label(frame, text="", wraplength=400, justify="left", font=("Arial", 14))
    label_texto.pack(pady=10)

    # Label para la imagen
    label_imagen = tk.Label(frame, text="[Imagen aquí]")
    label_imagen.pack(pady=10)

    # Botones para opciones
    botones_frame = tk.Frame(frame)
    botones_frame.pack(pady=10)

    # Creamos 3 botones (máximo 3 opciones)
    for _ in range(3):
        boton = tk.Button(botones_frame, text="", width=40, state="disabled")
        boton.pack(pady=5)
        botones.append(boton)

    # Botón para cerrar (opcional)
    boton_salir = tk.Button(frame, text="Salir", command=root.destroy)
    boton_salir.pack(pady=10)

    # Mostrar primer nodo
    nodo_actual_id = "inicio"
    historia_completa_gui = []
    mostrar_nodo_gui()

    # Inicia el bucle de eventos de Tkinter
    root.mainloop()


# =========================
# 5. PUNTO DE ENTRADA
# =========================

def main():
    """
    Menú simple para elegir versión de juego:
    - Consola
    - Gráfica (Tkinter)
    """
    print("El Constructor de Historias")
    print("1. Jugar en consola")
    print("2. Jugar con ventana gráfica (Tkinter)")

    eleccion = input("Elige 1 o 2: ").strip()
    if eleccion == "1":
        jugar_consola()
    else:
        iniciar_gui()


if __name__ == "__main__":
    main()
