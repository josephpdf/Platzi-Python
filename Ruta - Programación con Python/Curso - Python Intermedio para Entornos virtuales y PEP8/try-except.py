class DivisionError(Exception):
    """Error en operación"""

    pass


a = 0
b = 0

try:
    a = int(input("Digita un número: "))
    b = int(input("Digita otro número: "))
    if b == 2:
        raise Exception(
            "No se permiten números iguales a 2"
        )  # Lanza una excepción personalizada
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:  # Captura el error de conversión de tipo
    print("El valor que digitó no es un número válido")
except ZeroDivisionError:
    print("No está permitido dividir por 0")
finally:  # Se ejecuta siempre, haya o no un error
    print("Esto se ejecuta siempre, haya o no un error")

print("Fin del programa")
