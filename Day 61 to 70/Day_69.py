''' 
100 Dias De Python - Dia 69
---------------------------
Utiliza regex para extraer todas las 'a' seguidas de una o mas b's de la cadena
cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"
imprime unalista con las subcadenas extraidas
'''
import re 

cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"
subcadenas= re.findall('(a+b)',"abholaaaaabaaabbpythonistaaaaaabbbbb")
print(subcadenas)
