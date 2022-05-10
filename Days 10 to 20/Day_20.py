# 100DiasDePython
# Dia_20
# De la siguiente cadena: 'PpYyTtHhOoNnIiSsTtAa' separa las mayusculas y minusculas 
# sin usar ciclos en nuevas cadenas e imprime el resultado en una sola linea. 
# Alberto Bueno (babuenop)#6398

s="PpYyTtHhOoNnIiSsTtAa"
lower=filter(str.islower,s)
upper=filter(str.isupper,s)
s1="".join(lower)
s2="".join(upper)
print (s1 +" "+ s2)
#Output: pythonista PYTHONISTA

# Solucion @pythonlapaz
a="hjfacetiluzislcafiesdolavedfiedesno"
minusculas=s[::2]
mayusculas=s[1::2]
print(minusculas, mayusculas)