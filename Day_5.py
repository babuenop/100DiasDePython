# 100DiasDePython
# Dia_5
# Declara una lista de numeros y encuentra el valor mas pequeño

lista = [-5,-4,0,2,1,-3]
menor=lista[0]

for i in lista:
    if lista[i]<menor:
        menor=lista[i]
print(menor)

# Otra solución
lista = [0,1,0,2,1,3]
print(min(lista))