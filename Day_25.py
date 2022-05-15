# 100DiasDePython
# Dia_24
# Utiliza la lista de compras del reto anterior para contruir una cadena con saltos de linea. 
# sin usar ciclos e imprime el resultado
# Alberto Bueno (babuenop)#6398

lista = ['Tomate', 'Pepino', 'Piña', 'Narajas', 'Leche', 'huevos']
# str= lista[0] + '\n' + lista[1] + '\n' + lista[2] + '\n' + lista[3] + '\n' +lista[4]
# print(str)

''' Solucion Correcta '''
str = '\n'.join(lista)
print(str)