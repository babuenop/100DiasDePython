''' 
100 Dias De Python - Dia 93
---------------------------
Crea una funcion que use yield y genere los primeros 10 numeros de la serie fibonacci. 
Imprime el resultado en una lista
'''

def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))
