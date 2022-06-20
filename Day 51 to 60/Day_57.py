''' 
100 Dias De Python - Dia 57
---------------------------
Utiliza una funcion lambda para encontrar los multiplos de 3 en una lista de numeros
'''
import math

my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = list(filter(lambda x: x % 3 ==0 , my_list))

print(new_list)









    
    
    

