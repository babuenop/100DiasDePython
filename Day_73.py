''' 
100 Dias De Python - Dia 73
---------------------------
Utiliza itertools para obtener todas las permutaciones posibles con las letras de la lista. 
Imprime el resultado en una lista de tuplas
'''
import itertools
lista = ["r", "i", "o"]
result=list(itertools.permutations(lista))
print(result)


