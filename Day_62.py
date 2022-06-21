''' 
100 Dias De Python - Dia 62
---------------------------
Utiliza regex para validar la lista de emails 
Imprime una lista con los email validos
'''
import re 

correos = ['pythonlapaz@gmail.com', 'dias.com', 'comidita@.com', 'programando@outlook.com']
patron = '^\S+@\S+\.\S+$'
validos = [c for c in correos if re.search(patron, c)]
print(validos)
