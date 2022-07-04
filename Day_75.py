''' 
100 Dias De Python - Dia 75
---------------------------
Utiliza itertools para obtener el mensaje secreto en la cadena
Imprime el resultado en una cadena
'''
import itertools
cadena = "P1y2t3h4o5n6!7"
mensaje = ""
mensaje = mensaje.join(itertools.islice(cadena,0, None,2))
print(mensaje)