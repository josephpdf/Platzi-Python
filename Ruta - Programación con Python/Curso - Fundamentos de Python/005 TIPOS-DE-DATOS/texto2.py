# ind - 01234...
texto = "Este es un texto"

# Slicing
print(texto[0]) # Output: E
print(texto[0:4]) # Output: Este 
print(texto[:7]) # Output: Este es
print(texto[5:10]) # Output: es un
print(texto[5:-2]) # Output: Este es un tex

print(texto[:-2]) 
print("")

# Método replace() reemplaza una palabra por otra
curso = "Este curso es de Javascript, Javascript"
print(curso.replace("Javascript", "Python"))
print("")

# Método split() divide el texto en una lista de palabras, usando el espacio como separador por defecto
textoDividido = texto.split(" ")
print(textoDividido)
print("")

# Normalización de texto para evitar problemas de mayúsculas y minúsculas
texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print("mayusculas" in texto2) # Output: False, porque "MAYUSCULAS" está en mayúsculas
print(texto2)
print("mayusculas".lower() in texto2.lower())
print(texto2.lower())
print(texto2.upper())