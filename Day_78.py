''' 
100 Dias De Python - Dia 78
---------------------------
Utiliza itertools para unir las tuplas 
Obtener el tipo de cada dato e imprimelo en una lista
'''
import itertools
a, b = (78, 100) , ("Dias", "Python")
lista = list(itertools.chain(a, b))
tipos = list(type(k) for k in lista)
print(tipos)

