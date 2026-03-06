x = 1 # Entero (int)
y = 2.5 # Flotante (float)
z = 1j # Imaginario (complex)

print(type(x))
print(type(y))
print(type(z))

positivo = 5.5
negativo = -5.5

imaginario = -5 - 1j

xf = float(x) # Convertir entero a flotante (casteo o coerción) 

print(type(xf))
print(xf)

ye = int(y) # Convertir flotante a entero (truncamiento)

print(type(ye))
print(ye)

entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo)
print(type(enteroComplejo))
print(flotanteComplejo)
print(type(flotanteComplejo))

import random # Módulo para generar números aleatorios

print(random.randrange(1, 10)) # Output número aleatorio entre 1 y 9