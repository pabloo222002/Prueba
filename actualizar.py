import random
from datetime import datetime

# Archivo que deseas modificar
archivo = "Videojuego en C"

# Lista de mensajes aleatorios
mensajes = [
    "Optimización de funciones.",
    "Pequeña mejora en el código.",
    "Actualización del proyecto.",
    "Agregando nuevos comentarios.",
    "Limpieza de código y refactorización."
]

# Selecciona un mensaje aleatorio
mensaje = random.choice(mensajes)

# Agrega un comentario con la fecha y el mensaje al archivo
with open(archivo, "a") as f:  # "a" significa "append", agrega al final del archivo
    f.write(f"\n// {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {mensaje}\n")

print(f"Se agregó al archivo: {mensaje}")
