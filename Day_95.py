''' 
100 Dias De Python - Dia 93
---------------------------
Crea una funcion que use argumentos arbitrarios para recibir N-numeros y determine cual es el mayor y el menor  y los devuelva en un diccionario en el siguiente formato
{"mayor":5, "menor":-10}
Imprime el resultado 
'''

def funcion(*args):
    lista = [*args]
    resultado = {"mayor": max(lista), "menor":min(lista)}
    return(print(resultado))     
       
funcion(9, 10,-1,3,5,-2,8)

