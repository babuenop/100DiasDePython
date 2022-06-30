''' 
100 Dias De Python - Dia 68
---------------------------
Utiliza regex para cambiar el formato de las fechas de YYYY-MM-DD a DDMMYYYY de las fechas de la lista
Imprime una lista con las fechas
'''
import re 

fechas = ['2022-12-05','1993-06-12', '2005-01-26','2021-10-08']
validos = [re.sub(r'(\d{4})\-(\d{2})\-(\d{2}).*',r'\3\2\1', fecha) for fecha in fechas]
print(validos)
