''' 
100 Dias De Python - Dia 64
---------------------------
Utiliza regex para quitar los ceros innecesarios de las direcciones IP de la lista
Imprime una lista con las IPs validas 
'''
import re 

ips = ['192.08.001.5','10.120.023.001','192.160.2.1']
patron = "^\w*$"
ips_validas = [c for c in ips if re.search(patron, c)]
print(ips_validas)
