''' 
100 Dias De Python - Dia 76
---------------------------
Utiliza itertools para obtener el valor maximo de cada tupla de la lista
Imprime el resultado en una lista
'''
import itertools
lista = [(2,4,6),(7,8,5,6),(5,10)]
maximos= list(max(lista) for lista ,k in itertools.groupby(lista))
print(maximos)