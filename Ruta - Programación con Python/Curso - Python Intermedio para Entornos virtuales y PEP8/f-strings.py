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
