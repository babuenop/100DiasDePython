''' 
100 Dias De Python - Dia 65
---------------------------
Utiliza regex para quitar los prefijos telefonicos de los telefonos de la lista
Imprime una lista con los telefonos sin prefijos telefonicos
'''
import re 

telefonos  = ['+54 11 1234 5678', '+591 6874321', '+56 9 8765 4321']
validos = [re.sub('\+\d+\s+','',telefono) for telefono in telefonos]

print(validos)
