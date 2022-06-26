''' 
100 Dias De Python - Dia 67
---------------------------
Utiliza regex para cambiar el formato de las fechas de YYYYMMDD a YYYY-MM-DD de las fechas de la lista
Imprime una lista con las fechas
'''
import re 

fechas = ['20221205','19930612', '20050126','20211008']
validos = [re.sub(r'(\d{4})(\d{2})(\d{2}).*',r'\1-\2-\3', fecha) for fecha in fechas]
print(validos)
