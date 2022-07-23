''' 
100 Dias De Python - Dia 93
---------------------------
Crea una funcion que use argumentos arbitrarios para recibir n-cadenas de nombres y devuelva una lista de N saludos 
Imprime el resultado en una lista
'''

def saludos(*args):
    for i in range(len(args)):
        lista = ["Hola "+args[i] for i in range(len(args))]
        return(print(lista))        
saludos("Katy","Ariel")