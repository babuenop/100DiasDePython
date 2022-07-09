''' 
100 Dias De Python - Dia 80
---------------------------
Utiliza itertools para repetir el numero 80 5 veces en una lista
Imprime el resultado en una lista
'''
from itertools import repeat

lista = list(repeat(80,5))

print(lista)
