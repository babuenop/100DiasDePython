''' 
100 Dias De Python - Dia 91
---------------------------
Crea una funcion que devuelva los cuadrados de los primeros 10 numeros enteros iniciando en 1, utilizando yields 
Imprime el resultado en una lista
'''

def Square():
    i = 1
    while True:
        yield i*i                
        i += 1
                  
for num in Square():
    if num > 100:
         break    
    print(num)