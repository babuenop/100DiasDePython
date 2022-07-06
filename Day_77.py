''' 
100 Dias De Python - Dia 77
---------------------------
Utiliza itertools para obtener los multiplos de 5 de la siguiente lista
Imprime el resultado en una lista
'''
import itertools
lista =[1, 5, 10, 23, 3, 555, 11, 10]
multiplos = list(itertools.filterfalse(lambda x: x%5, lista))
print(multiplos)

