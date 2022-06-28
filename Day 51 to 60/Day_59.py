''' 
100 Dias De Python - Dia 59
---------------------------
Utiliza una funcion lambda para ordenar de forma ascendente la siguiente lista de tuplas tomando en cuenta el valor numerico como referencia. 
[("Quimica",88), ("Fisica",90)("Lenguaje",97)]
Imprime el resultado
'''

list = [("Quimica",88), ("Fisica",90),("Lenguaje",97)]
list.sort(key=lambda x:x[1])
print(list)







    
    
    

