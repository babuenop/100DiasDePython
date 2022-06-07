''' 
100 Dias De Python - Dia 48
------------------------
Con un rango de 5 numeros crea una lista que refleje con valores boleanos cuales son pares e imprime el resultado. 
Alberto Bueno (babuenop)#6398 

'''

numeros = list(range(1,6))
pares = []
for i in numeros:
    if i % 2 == 0 :
       pares.append(True)
    else:
       pares.append(False)
print(numeros)
print(pares)


