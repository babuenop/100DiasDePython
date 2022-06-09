''' 
100 Dias De Python - Dia 48
------------------------
Genera 5 numeros enteros de forma aleatoria almacenalos en una lista, sumalos e imprime el resultado. 
Alberto Bueno (babuenop)#6398 

'''
import random

randomlist = random.sample(range(1, 10), 5)
suma = 0

for i in randomlist:
    suma += i

print(randomlist)
print(suma)

