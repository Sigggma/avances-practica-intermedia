import ctypes

# Cargamos la biblioteca compartida
lib = ctypes.CDLL('./holamundo.dll')  # En Windows

# Llamamos a la función hola_mundo desde la biblioteca
lib.hola_mundo()
