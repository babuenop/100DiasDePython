''' 
100 Dias De Python - Dia 83
---------------------------
Utiliza datetime para convertir la fecha "Jul 11 2022 1:30AM" en el formato "2022-07-11 01:30:00"
Imprime el resultado
'''
from datetime import datetime
fecha = datetime.strptime('Jul 11 2022 1:30AM', '%b %d %Y %I:%M%p')
print(fecha)
