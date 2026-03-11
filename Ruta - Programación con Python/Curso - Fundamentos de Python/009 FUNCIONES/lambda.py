# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero sólo una expresión
# Sintaxis lambda argumentos : expresión 

x = lambda a : a + 10
print(x(5)) # 15

print("---------------")
x = lambda a, b : a + b
print(x(2,3)) # 5

print("---------------")
def mifuncion(n):
    return lambda a : a * n # La función mifuncion devuelve una función lambda que multiplica su argumento a por n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

print(duplicador(5)) # 10
print(triplicador(5)) # 15

# Desafio
quintuplicador = mifuncion(5)

print(quintuplicador(5)) # 25