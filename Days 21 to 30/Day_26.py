''' 
100DiasDePython - Dia_26    
------------------------

Utiliza la funcion copy() para crear una copia de la lista de compras
Compara sus ids en memoria e imprime el resultado 
Alberto Bueno (babuenop)#6398 

'''

lista = ['Tomate', 'Pepino', 'Piña', 'Narajas', 'Leche', 'huevos']
copia = lista.copy()
print(id(lista) == id(copia))


