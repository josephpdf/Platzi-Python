x = 5
y = 3
z = 10

if x > y:
    print(x, "es mayor a", y)
# if y > x:
    # print("No se va a cumplir")
elif x == y: # Evaluar segunda condición, si la anterior no se cumple
    print(x, "es igual a", y)
else: # Si ninguna de las condiciones anteriores se cumple, se ejecuta el bloque de código del else
    print("Ninguna de las condiciones anteriores se cumplió")

# Podemos anidar estructuras condicionales
if x > y and x > z:
    print("x es mayor a y y x es mayor a z")
elif x == y:
    print("x es igual a y")
else:
    print("Ninguna de las condiciones anteriores se cumplió")

if x > y or x > z:
    print("x es mayor a y o x es mayor a z")
elif x == y:
    print("x es igual a y")
else:
    print("Ninguna de las condiciones anteriores se cumplió")

# Compaar cadenas de texto
a = "Python"
b = "Javascript"
c = "Python"

if a == b:
    print("a es igual a b")
else:
    print("a es distinto a b")

if a == c:
    print("a es igual a c")
else:
    print("a es distinto a c")

# Anidar estructuras condicionales
if a == c:
    if a != b:
        print("a es igual a c pero es distinto a b")
    else:
        print("Estoy saliendo por el else del if interno")
else:
    print("a no es igual a c")

if a == c:
    if a == b:
        print("a es igual a c pero es distinto a b")
    else:
        print("Estoy saliendo por el else del if interno")
else:
    print("a no es igual a c")

# Otras condiciones
e = 10
f = 10

if e == f:
    pass # Para ignorar la estructura if hasta tanto definamos que comportamiento se espera