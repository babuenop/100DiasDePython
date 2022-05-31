''' 
100 Dias De Python - Dia 36
------------------------
Utiliza el diccionario de palabras del reto anterior para eliminar el primer elemento del diccionario 
Imprime la cantidad de elementos del diccionario. 
Alberto Bueno (babuenop)#6398 

'''

Words = {
    "Atributo" : "Componente que tienen las clases para almacenar informacion",
    "Booleano" : "Tipo de datos logico que se caracteriza porque unicamente debe tener dos valores, ó True ó False",
    "Clase" : "Tipo de datos que define un conjunto de atributos y métodos", 
    "Metodo" : "Componente de una clase que aporta funcionalidad a la misma",
    "Tupla" : "Conjunto ordenado e inmutable de elementos. Las tuplas pueden contener elementos de diferentes tipos",
    "Objeto" : "Instancia de una clase",
    }

del Words["Clase"]
print(len(Words))


