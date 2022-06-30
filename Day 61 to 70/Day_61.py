''' 
100 Dias De Python - Dia 61
---------------------------
Utiliza regex para validar que las cadenas de la lista sean totalmente numericas. 
Imprime el resultado
'''
import re 

lista = ['20200806', 'jun122022', '202204DD', '20221208', '22mar2022']
x = []

for i in lista:
    x = x + re.findall('^[0-9]*$', i)
print(x)
