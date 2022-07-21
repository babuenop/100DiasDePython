''' 
100 Dias De Python - Dia 91
---------------------------
Crea una funcion que utilice yield y genere la siguiente serie [1,2,3,2,1,2,3,2,1]
Imprime el resultado en una lista
'''

def gen():
    yield from [1,2,3,2,1,2,3,2,1]

lista = list(gen())
print(lista)

