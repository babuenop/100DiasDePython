''' 
100 Dias De Python - Dia 60
---------------------------
Utiliza una funcion lambda para capitalizar las palabras de la lista
Imprime el resultado
'''

lista = ['llevo', 'sesemta', 'dias', 'programando', 'wii']
result = map(lambda x:  x.capitalize(), lista)
print(list(result))
