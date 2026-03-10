palabra = "Python"

for letra in palabra:
    print(letra)

adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Naranja", "Kiwi"]

print("-------------------------")
# Lista de frutas
for fruta in frutas:
    print(fruta)

print("-------------------------")
# Lista de frutas con break
for fruta in frutas:
    if fruta == "Naranja":
        break
    print(fruta)

print("-------------------------")
# Lista de frutas con continue
for fruta in frutas:
    if fruta == "Naranja":
        continue
    print(fruta)
else:
    print("Ya hemos terminado el bucle for")

print("-------------------------")
for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)

# Desafio
# Manzana Rica
# Manzana Saludable
# Naranja Rica
# Naranja Saludable
# Kiwi Rica
# Kiwi Saludable

print("-------------------------")
for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)

print("-------------------------")

# Range

# Comienza desde el cero y termina en el número que asignemos sin incluírlo
for i in range(10):
    print(i)

print("-------------------------")
# Comienza desde el número que asignemos y termina en el número que asignemos sin incluírlo
for i in range(3,5):
    print(i)

print("-------------------------")
# Comienza desde el número que asignemos, termina en el número que asignemos sin incluírlo y se incrementa en el número que asignemos
for i in range(0,11,2):
    print(i)

print("-------------------------")
# Pass es una palabra reservada que se utiliza cuando no queremos ejecutar ninguna acción dentro de un bloque de código, pero necesitamos que el bloque exista por alguna razón (por ejemplo, para evitar errores de sintaxis).
for i in range(10):
    pass