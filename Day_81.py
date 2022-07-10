''' 
100 Dias De Python - Dia 81
---------------------------
Utiliza datetime para agregarle a la fecha actual 7 dias mas 
Imprime el resultado 
'''

import datetime
fechaActual = datetime.date.today()
delta = datetime.timedelta(days=7)
fechaFinal= fechaActual + delta
print(fechaFinal)