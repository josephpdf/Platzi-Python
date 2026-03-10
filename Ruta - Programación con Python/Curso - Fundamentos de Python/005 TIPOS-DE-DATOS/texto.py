from math import sin

print('Hola "Mundo"')

ingles = "I'm Sergie"

multiples = """Hola
Mundo
desde
las
comillas
triples"""

print(ingles)
print(multiples)

palabra = "Murciélago"
print(len(palabra)) # Cuenta el número de caracteres, incluyendo acentos y caracteres especiales

texto = "Este curso es de Fundamentos de Python"
estaIncluda = "Python" in texto # Verifica si la palabra "Python" está incluida en el texto
noEstaIncluida = "Javascript" not in texto # Verifica si la palabra "Javascript" NO está incluida en el texto

print(noEstaIncluida)

mayuscula = texto.upper() # Convierte el texto a mayúsculas
minuscula = texto.lower() # Convierte el texto a minúsculas

print(mayuscula)
print(minuscula)

texto2 = texto.upper()
texto2 = texto.lower() # Si se usan varias variables, la ultima predomina

print(texto2)

espacios = "        Este es el texto         "
sinEspacios = espacios.strip() # Elimina los espacios en blanco al inicio y al final del texto

print(sinEspacios)