''' 
100 Dias De Python - Dia 88
---------------------------
Utiliza calendar para imprimir la cantidad de semanas de cada mes del año 2022
'''
import calendar
cal = [len(calendar.monthcalendar(2022,i)) for i in range(1,12)]
print (cal)