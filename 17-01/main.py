import ctypes
from platform import system

# Cargamos la biblioteca compartida
if system() == "Windows":
    lib = ctypes.CDLL("./holamundo.dll")  # En Windows
else:
    lib = ctypes.CDLL("./holamundo.so")  # En Linux/macOS

# Llamamos a la función hola_mundo desde la biblioteca
lib.hola_mundo()
