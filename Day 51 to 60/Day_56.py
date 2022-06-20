''' 
100 Dias De Python - Dia 56
---------------------------
Funcion lambda ppara encontrar la raiz cuadrada de una lista de numeros
'''
import math

my_list = [49,4,36,16,25]

new_list = list(map(lambda x: math.sqrt(x) , my_list))

print(new_list)









    
    
    

