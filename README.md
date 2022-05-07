# 100 Dias De Python 
100 Dias de Python con la comunidad de @PythonLaPaz

En la carpeta pruebas se encuentran practicas extra que he encontrado como complemento de practica a estos 100 dias del reto. 

# Dia 1
## Declarar una variable numerica e imprimirla. 

En Python las variable numericas son usadas para almacenar numeros. 
Los numeros son usualmente almacenados como Enteros o Numeros Reales 

*Integers* o numeros enteros son aquellos numeros que no tienen decimales y pueden ser positivos o negativos, incluyendo al 0.

Los numeros enteros se representan en Python como **int**

*Floating-point values* Son aquellos numeros que tinen decimales. En Python se representan como **float** y la separacion entre la parte entera y la parte decimal se realiza con un punto. 

# Dia 4 Funcion Type() 

type() method returns class type of the argument(object) passed as parameter. type() function is mostly used for debugging purposes.

Two different types of arguments can be passed to type() function, single and three argument. If single argument type(obj) is passed, it returns the type of given object. If three arguments type(name, bases, dict) is passed, it returns a new type object.

`
type(object)
type(name, bases, dict)
`

Parameters :
name : name of class, which later corresponds to the __name__ attribute of the class.
bases : tuple of classes from which the current class derives. Later corresponds to the __bases__ attribute.
dict : a dictionary that holds the namespaces for the class. Later corresponds to the __dict__ attribute.


## Day 15 Funcion Slice 

**Syntax**
```slice(start, end, step)```

**Parameter Values**
| Parameter | Description |
| ----------- | ----------- |
| Start | Optional. An integer number specifying at which position to start the slicing. Default is 0 |
| end | An integer number specifying at which position to end the slicing |
| step | Optional. An integer number specifying the step of the slicing. Default is 1 |

**Example**
```Python
variable = "Germany'
print(variable[-3:])
amy
```

## Day 16 String count() Method

**Syntax**
```slice(start, end, step)```

**Parameter Values**
| Parameter | Description |
| ----------- | ----------- |
| Start | Required. A String. The string to value to search for |
| end | Optional. An Integer. The position to start the search. Default is 0 |
| step | Optional. An Integer. The position to end the search. Default is the end of the string |

**Example**
```Python
# 100DiasDePython
# Dia_16
# Declara una variable de tipo cadena, encuentra la cantidad de veces que aparece la letra a
# Alberto Bueno (babuenop)#6398

variable = "Vamos a contar las letras a que aparecen en esta cadena"
print(variable.count('a'))

#Ressultado= 11
```


