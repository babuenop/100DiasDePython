''' 
100 Dias De Python - Dia 52
---------------------------
Crea una funcion que convierta un numero entero en binario. 

'''
binario = []

def dec_a_bin (a: int):
    '''
    Funcion que convierte un numero entero en binario. 
    Args:
        a : Numero decimal 
    Returns: 
        valor binario
    '''

    if a == 0:
        binario.insert (0, 0)
    while a != 0 :
        binario.insert (0, a % 2)
        a = int(a / 2)
    print (''.join(str(x) for x in binario))    

dec_a_bin(52)










    
    
    

