# open(nombre, modo) # Manipular archivos 
# Modos de apertura de archivos
# R (read) Lectura 
# W (write) Escritura
# X (Crea archivo nuevo)

# Crear un archivo nuevo con with
try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x")
    print("No se ha encontrado el archivo")

print("-----------------------------")
try:
    f = open("archivo.txt", "r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo")

print("-----------------------------")
# With es un manejador de contexto, se encarga de abrir y cerrar el archivo automáticamente
# Leer un archivo con with
try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")

print("-----------------------------")
# Escribir en un archivo con with
try:
    with open("archivo.txt", "w", encoding="utf-8") as f:
        f.write("Hola mundo desde write en el with")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")

print("-----------------------------")
# Agregar contenido a un archivo con with
try:
    with open("archivo.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("Hola mundo desde append en el with")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")