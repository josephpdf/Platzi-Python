# Coleccion de pares clave calor (Ordenado a partir de Python 3.7)

auto = {
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}

print(auto)
print(auto["marca"])
print(auto.get("marca")) # Si la clave no existe, devuelve None en lugar de lanzar un error

print(auto.keys()) # Obtener las claves del diccionario
print(auto.values()) # Obtener los valores del diccionario

if "marca" in auto: # Verificar si una clave existe en el diccionario
    print("Marca es una de las propiedades de este diccionario")

auto["año"] = 2020 # Modificar el valor de una clave existente
print(auto)

auto["color"] = "Verde" # Agregar una nueva clave-valor al diccionario
print(auto)

auto.update({"año": 2022, "puertas": 4}) # Modificar el valor de una clave existente y agregar una nueva clave-valor al diccionario
print(auto)

# auto.pop("puertas") # Eliminar una clave-valor del diccionario
# print(auto)

# auto.popitem() # Eliminar el último par clave-valor agregado al diccionario
# print(auto)

# auto.clear() # Eliminar todos los pares clave-valor del diccionario, dejando un diccionario vacío
# print(auto)

for k in auto: # Keys
    print(k)

print("---------------")
for v in auto.values(): # values
    print(v)

print("---------------")
for k,v in auto.items(): # keys, value
    print(k, "-" ,v)

print("---------------")
# Diccionarios Anidados
familia = {
    "hijo1" : {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2" : {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3" : {
        "nombre": "Marcelo",
        "edad": 6
    }
}

print(familia["hijo1"]["nombre"])