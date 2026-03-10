# Operadores de Comparación
x = 5
y = 3
z = 5

print("x es igual a y:", x == y) # ¿Si es igual? False
print("x es distinto de y:", x != y) # Si es distinto True
print("x es mayor que z:", x > z) # Es mayor a segunda True
print("x es menor que y:", x < y) # Es menor False
print("x es mayor o igual que z:", x >= z) # Es mayor o igual True
print("x es menor o igual que y:", x <= y) # Es menor o igual False

# Operadores lógicos

#                                              True     False
print("x es mayor que y y y es mayor que z:", x > y and y > z) # False
print("x es mayor que y o y es mayor que z:", x > y or y > z) # True

v = True
f = False

print("Negación de v:", not(v))
print("Negación de f:", not(f))