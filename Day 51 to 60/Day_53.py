''' 
100 Dias De Python - Dia 53
---------------------------
Crea una funcion que reciba una lista de numeros y devuelva una lista de los numeros al cuadrado.
Ejecuta la funcion para la lista be kind your mind 

'''
lista = [2,3,5,7,11]
lista_cuadrados = []

def lista_al_cuadrado (a):
    '''
    Funcion que devuelve una lista de los numeros cuadrados 
        lista 
    Return: 
        lista_cuadrados 
    '''
    for i in lista:
        lista_cuadrados.append( i**2 )
    return lista_cuadrados

lista_al_cuadrado(lista)
print(lista_cuadrados)











    
    
    

