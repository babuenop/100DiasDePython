''' 
100 Dias De Python - Dia 81
---------------------------
Utiliza datetime para imprimir la fecha y hora actual en el formato 
"10 July 2022, 12:12:12 AM"
Imprime el resultado en una cadena
'''
from datetime import datetime
  
time = datetime.now()
formatingDate = time.strftime("%d %B %Y, %l:%M:%S %p")  
print(formatingDate)
