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
        vocales = 0
        for n in "aeiou":
            vocales += cadena.count(n)    
            salida[cadena] = vocales
    return (salida)

entrada=['Python', 'es', 'cool']
print(cuenta_vocales(entrada))

        













    
    
    

