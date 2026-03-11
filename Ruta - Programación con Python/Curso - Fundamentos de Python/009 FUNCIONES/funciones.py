# Función: es un bloque de código que solo se ejecuta cuando la llamamos. Permiten organizar y modularizar el código (reutilización)
def mi_funcion(): # Definición de la función
    print("Hola Mundo desde una función")

mi_funcion() # Llamada a la función

print("---------------")
def saludar(nombre, apellido=""): # Argumentos: son los valores que se pasan a la función para que esta los utilice en su ejecución
# Se declara vacio para que no gene un error si no se envía un valor para ese argumento
    print("Hola", nombre, apellido)

saludar("Joseph", "Poveda") # Parámetros: son los valores que se definen en la función para recibir los argumentos
# Siempre enviar todos los argumentos que la función espera, de lo contrario se producirá un error

print("---------------")
def saludar2(nombre, nacionalidad="Costa Rica"): # Argumentos
    print("Hola", nombre,"de", nacionalidad)

saludar2("Pedro", "España") # Parámetros
saludar2("Joseph")

print("---------------")
def sumar(a,b):
    return a + b # La función devuelve el resultado de la suma de a y b, pero no lo imprime. Para ver el resultado, debemos imprimirlo al llamar a la función

resultado = sumar(2,3) # Llamada a la función sumar con los argumentos 2 y 3, y se almacena el resultado en la variable resultado
print(resultado)

def funcion(): # Una función sin argumentos ni valor de retorno
    pass # La palabra reservada pass se utiliza para indicar que no se va a ejecutar ningún código dentro de la función, pero se mantiene la estructura de la función para que no genere un error.

print("---------------")
# Desafio de operacionnes matematicas
def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b != 0: # Verificar que el divisor no sea cero para evitar un error de división por cero
        return a / b
    else:
        return "ERROR: No se puede dividir por cero"
    
resta = restar(10,5)
multiplicacion = multiplicar(10,5)
division = dividir(10,0)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)