''' 
100 Dias De Python - Dia 96
---------------------------
Crea una funcion que use argumentos arbitrarios de tipo keyword para recibir nombre, apellido, y edad y devuelva estos argumentos en un diccionario en el formato 
{"nombre":"pepito", "apellido": "perez", "edad":25}
Imprime el resultado 
'''

def funcion(nombre, apellido, edad):
    resultado = {"nombre": nombre, "apellido":apellido, "edad":edad}
    return(print(resultado))     
       
funcion(apellido="Garcia", nombre="Jinneth", edad=40)

