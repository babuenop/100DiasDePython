''' 
100 Dias De Python - Dia 63
---------------------------
Utiliza regex para validar que las cadenas de la lista solo contengan caracteres alfanumericos. 
Imprime una lista con las cadenas validas
'''
import re 

correos = ['python3.10', 'Python3', 'ProgramAndoAndo', 'jun2022', '#100diasdecodigo', 'Felicidades']
patron = "^[a-zA-Z0-9_]*$"
validos = [c for c in correos if re.search(patron, c)]
print(validos)
