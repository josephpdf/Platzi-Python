# Sintaxis básica de manejo de errores en Python
# try:
#     print("Intentamos ejecutar este bloque de código")
# except:
#     print("Si ocurre un error, se ejecuta este bloque")

try:
    numero = 10 / 0
except:
    print("Captura error")

print("----------------------------")
try:
    numero = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

print("----------------------------")
x = 1

try:
    print(x)
except NameError:
    print("Esta variable no ha sido definida")
finally:
    print("Esto será ejecutado siendo exitoso o no el bloque")