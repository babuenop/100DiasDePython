''' 
100 Dias De Python - Dia 89
---------------------------
Utiliza calendar para obtener los dias lunes del mes de Julio del año 2022
'''

import calendar
obj = calendar.Calendar()
list =[day for day in obj.itermonthdays(2022, 7)][0:31:7]
mondays =[(i) for i in list if i!=0]
print(mondays)
