# Texto (string)
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples1 = """comillas triples"""
comillasTriples2 = '''comillas triples'''

print(comillasSimples)
print(comillasDobles)
print(comillasTriples1)
print(comillasTriples2)

# Números
a = 1
b = 3.14
c = 5 + 2j

print(a)
print(b)
print(c)

# Lista
lista = [0,1,2,3,4,5] # Mutable, se pueden modificar sus elementos

# Tupla
tupla = ("a","b","c") # Inmutable, no se pueden modificar sus elementos

# Diccionario, Objetos Literales
diccionario = { # Mutable, se pueden modificar sus elementos
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Conjuntos (sets) Desordenados, no permiten elementos duplicados, mutable, no permiten indexación
conjunto = {1,1,2,2,3} # Output: {1,2,3}

# booleanos (True o False)
booleanoVerdadero = True
booleanoFalso = False