''' 
100 Dias De Python - Dia 71
---------------------------
Utiliza itertools para generar una serie de sumas con los numeros de la lista
Imprime el resultado
'''
import itertools
import operator

lista = [0, 1, 1, 2, 3, 5, 8]
result = list(itertools.accumulate(lista, operator.add)) 
print(result)