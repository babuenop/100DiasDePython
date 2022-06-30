''' 
100 Dias De Python - Dia 64
---------------------------
Utiliza regex para quitar los ceros innecesarios de las direcciones IP de la lista
Imprime una lista con las IPs validas 
'''
import re 


ip_adr  = ['192.08.001.5','10.120.023.001','192.160.2.1']
validos = []
for i in ip_adr:
    validos.append(re.sub('\.[0]*', '.', i))
print(validos)
