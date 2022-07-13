''' 
100 Dias De Python - Dia 84
---------------------------
Utiliza datetime para convertir la cadena "12-07-2022" a timestamp
Imprime el resultado
'''
import datetime
stime = "12-07-2022"
print(datetime.datetime.strptime(stime, "%d-%m-%Y").timestamp())