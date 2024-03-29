''' 
100 Dias De Python - Dia 72
---------------------------
Utiliza itertools para obtener la cantidad de veces que se repite cada numero en la lista
Imprime el resultado
'''
import itertools
 
from more_itertools import unique_everseen

lista = [0, 1, 1, 2, 3, 2, 4, 5, 5, 8, 4]
result = {k:lista.count(k) for k in unique_everseen(lista)}
print(result)

# o 
resultado={}
data = sorted(lista)
for k, g in itertools.groupby(data):
    resultado[k]= len(list(g))
print(resultado)
    