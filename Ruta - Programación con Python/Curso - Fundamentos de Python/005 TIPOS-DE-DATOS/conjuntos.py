# Conjunto (set): Colección NO ordenada de elementos únicos (no se puede accede por índice)

frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"} # conjunto no permite elementos duplicados
print(frutas)
print(type(frutas))
print(len(frutas))

print("-----------------------")

print("Manzana" in frutas)
print("Pera" not in frutas)

print("-----------------------")

# Agregar
# Add
frutas.add("Pera") # Agrega un elemento al conjunto, si el elemento ya existe no se agrega y no lanza error
print(frutas)

print("-----------------------")

# Update
frutasTropicales = { "Piña", "Mango"} 
frutas.update(frutasTropicales) # Agregar listas, tuplas, conjuntos
print(frutas)

print("-----------------------")

# Eliminarlos
# Remove
frutas.remove("Mango") # Elimina un elemento, si no existe lanza error
print(frutas)

print("-----------------------")

#Discard
frutas.discard("Banana") # Descartar un elemento, si no existe no lanza error
print(frutas)

print("-----------------------")

# Pop
frutas.pop() # Elimina un elemento aleatorio del conjunto
print(frutas)

print("-----------------------")

# Clear
frutas.clear() # Elimina todos los elementos del conjunto, el conjunto queda vacío pero sigue existiendo
print(frutas)

print("-----------------------")

conjuntos = {"Python", 156, True}
print(conjuntos)
print(type(conjuntos))

for item in conjuntos:
    print(item)

print("-----------------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

u = a.union(b) # Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos, sin duplicados
print(u)

i = a.intersection(b) # Devuelve un nuevo conjunto con los elementos que están en ambos conjuntos
print(i)

d = a.difference(b) # Devuelve un nuevo conjunto con los elementos que están en el primer conjunto pero no en el segundo
print(d)