''' 
100 Dias De Python - Dia 84
---------------------------
Utiliza datetime para calcular la cantidad de segundos que han pasado desde el inicio del reto considerando solo la fecha. 
Considera que el reto inicio el "20/04/2022" e imprime el resultado. 
'''
from datetime import datetime

ini = "20/04/2022"
fin = datetime.today().strftime('%d/%m/%Y')

d0 = datetime.strptime(ini,'%d/%m/%Y')
d1 = datetime.strptime(fin,'%d/%m/%Y')

delta = d1 - d0
segundos = delta.days * 86400

print(segundos)
