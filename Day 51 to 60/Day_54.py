''' 
100 Dias De Python - Dia 54
---------------------------
'''

salida = {}

def cuenta_vocales (lista):
    '''
    Función que recibe una lista de cadenas y devuelve un diccionario 
    con el numero de vocales de cada cadena. 
    args: lista de cadenas 
    return: dict
    '''
    for cadena in lista:
        contador = 0
        for vocal in "aeiou":
            contador += cadena.count(vocal)    
            salida[cadena] = contador
    return (salida)

entrada=['Python', 'es', 'cool']
print(cuenta_vocales(entrada))

        













    
    
    

