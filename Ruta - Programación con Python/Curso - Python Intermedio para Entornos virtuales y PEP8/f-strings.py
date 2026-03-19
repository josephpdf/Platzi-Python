import datetime

name = "Joseph"
year = 1993
text = f"Hola, {name}!"  # f-string: cadena formateada con variables
print(text)

print("-------------------------")

text_suma = f"Hola, la suma es: {3 + 5}"
print(text_suma)

print("-------------------------")

text_calculo = f"Hola {name}, tu edad es: {2026 - year}"  # Cálculo dentro de f-string
print(text_calculo)

print("-------------------------")

text_func = f"HOLA {name.upper()}"  # Llamada a función dentro de f-string
print(text_func)

print("-------------------------")

edad = 20
text_if = f"Hola {name}, eres {'mayor de edad' if edad >= 18 else 'menor de edad'}"  # Condicional dentro de f-string
print(text_if)

print("-------------------------")

bank_balance = 1200000000
text = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"
print(text)

print("-------------------------")

stock_price = 1.405
text = f"El valor del stock es: {stock_price:.1f}"
print(text)
text = f"El valor del stock es: {stock_price:.2f}"
print(text)

print("-------------------------")

user_id = 3
text = f"Su id es: {user_id:02d}"
print(text)

print("-------------------------")

product = "Laptop"
price = 1000

text = f"Producto: {product} | Precio: {price}"
print(text)

print("-------------------------")

text = f"Producto: {product:<15} | Precio: {price:>10}"  # Alineación a la izquierda
print(f"{text}\n{text}\n{text}")  # Repetimos el texto para mostrar la alineación

print("-------------------------")

from datetime import datetime

date = datetime(2024, 12, 5, 10, 10)
text = f"La fecha completa es: {date}"
print(text)

print("-------------------------")

date = datetime(2024, 12, 5, 10, 10)
text = f"La fecha completa es: {date: %A %d de %B de %Y a las %I:%M %p}"  # Formato personalizado para fecha
+print(text)
