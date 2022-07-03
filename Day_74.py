''' 
100 Dias De Python - Dia 74
---------------------------
Utiliza itertools para obtener el producto cartesiando de las listas
Imprime el resultado en una lista de tuplas
'''
import itertools
a = [1, 3, 5]
b = [2, 4, 6]
result=list(itertools.product(a , b))
print(result)

list(input)