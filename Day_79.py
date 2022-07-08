''' 
100 Dias De Python - Dia 78
---------------------------
Utiliza itertools para obtener los elementos de la lista hasta que alguno contenga un 0
Imprime el resultado en una lista
'''
from itertools import takewhile

def contiene_0 (k):
    substring = '0'
    if substring in str(k):
        return False
    else:
        return True
       
numeros = [2, 3, 5, 7, 13, 103, 25, 15, 45]

lista = list(takewhile(contiene_0,numeros))

print(lista)
