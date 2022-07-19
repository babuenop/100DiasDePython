''' 
100 Dias De Python - Dia 90
---------------------------
Utiliza datetime para imprimir la fecha y hora en formato de 12 horas. 
'''
from datetime import datetime

now = datetime.now()
string = now.strftime("%Y/%m/%d %I:%M %p")
print(string)