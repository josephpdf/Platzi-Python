# LISTAS: Las listas son ordenadas, modificables y permiten valores duplicados

# Índices:   0          1           2            3
frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
print(frutas)
print(type(frutas)) # El tipo de dato de una lista es "list"

print(frutas[1])

frutas[1] = "Banana"

print(frutas[1])
print(frutas)

print("-------------------------")

lista = ["Joseph Poveda", 12, True]
print(lista)
print(type(lista))

print(len(lista)) # La función len() nos devuelve la cantidad de elementos que tiene una lista
print(len(frutas))

print("-------------------------")

print(frutas[0:2]) # Slicing
print(frutas[:2])
print(frutas[1:])

print("-------------------------")

if "Manzana" in frutas: # Existe o no dentro de la lista
    print("La manzana está dentro de las frutas")

print("-------------------------")

# Indices      0        1       2
vehiculos = ["Auto", "Moto", "Avión"]

# Métodos 
# Append (agregar un elemento al final de la lista)
vehiculos.append("Barco") # Indice 3
print(vehiculos)

# Insert 
vehiculos.insert(1, "Bicicleta")
print(vehiculos)

# Remove
vehiculos.remove("Auto")
print(vehiculos)

# Pop
vehiculos.pop(1)
print(vehiculos)

# Sort
vehiculos.sort() # Ordena la lista alfabéticamente, si la lista contiene números los ordena de menor a mayor
print(vehiculos)

# Reverse
vehiculos.reverse() # Invierte el orden de la lista, no la ordena al revés, sino que invierte el orden actual de la lista
print(vehiculos)

print("-------------------------")

# Unir listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

print(coleccion1)
print(coleccion2)
coleccion1.extend(coleccion2)
print(coleccion1)
print(coleccion2)

print("-------------------------")