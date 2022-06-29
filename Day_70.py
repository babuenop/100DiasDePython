''' 
100 Dias De Python - Dia 70
---------------------------
Utiliza regex para extraer todas las palabras que contengan al menos una 'a' en la cadena
cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"
imprime unalista con las subcadenas extraidas
'''
import re 

cadena = "Llevas programando 70 dias seguidos"
subcadenas= re.findall('[a-zA-Z]*a[a-zA-Z]*', cadena)
print(subcadenas)
