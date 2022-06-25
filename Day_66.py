''' 
100 Dias De Python - Dia 66
---------------------------
Utiliza regex para eliminar los caracteres que no sean alfanumericos en las cadenas de la lista
Imprime una lista con las cadenas validas
'''
import re 

cadenas = ['python3.10', 'Python3', 'ProgramAndoAndo', 'jun2022', '#100diasdecodigo', 'Felicidades!']
validos = [re.sub('\W+','',telefono) for telefono in cadenas]
print(validos)
