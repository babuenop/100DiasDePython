''' 
100 Dias De Python - Dia 98
---------------------------
Utiliza timeit para obtener el tiempo de ejecucion de la funcion. 
Imprime el resultado en una sola linea

'''
import timeit

def lazy():
    suma=0
    for i in range(0,50000000):
        suma+=i

print(timeit.timeit(lazy))


