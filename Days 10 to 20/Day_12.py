# 100DiasDePython
# Dia_12
# Intercambia los valores de dos variables e imprime su ubicacion en memoria utilizando la funcion id()
# Alberto Bueno (babuenop)#6398

a=10
b="Hola"
a , b = b , a
print(id(a),id(b))

