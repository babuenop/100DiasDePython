''' 
100 Dias De Python - Dia 51
------------------------
Crea una funcion que calcule el volumen de un cilindro. 
Los parametros de entrada son base y altura. El valor de la salida es el volumen del cilindro. 
Ejecuta la funcion para el caso base=5, altura=7
Imprime el resultado. 
Alberto Bueno (babuenop)#6398 

'''
# volume = π · r2 · h
from math import pi

def volume(b, a):
    radio = b/2
    return (pi * (radio)**2 * a)

result = volume(5,7)

print(result)
    
    
    

