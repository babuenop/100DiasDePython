''' 
100 Dias De Python - Dia 35
------------------------
Utiliza el diccionario de palabras del reto anterior para agregar una nueva palabra y su definicion. 
Imprime la cantidad de elementos del diccionario. 
Alberto Bueno (babuenop)#6398 

'''

Words = {
    "Atributo" : "Componente que tienen las clases para almacenar informacion",
    "Booleano" : "Tipo de datos logico que se caracteriza porque unicamente debe tener dos valores, ó True ó False",
    "Clase" : "Tipo de datos que define un conjunto de atributos y métodos", 
    "Metodo" : "Componente de una clase que aporta funcionalidad a la misma",
    "Tupla" : "Conjunto ordenado e inmutable de elementos. Las tuplas pueden contener elementos de diferentes tipos"
    }

Words["Objeto"]="Instancia de una clase"
print(len(Words))