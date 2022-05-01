import string 
d= {x:y for x,y in enumerate(list(string.ascii_lowercase),1)}
print(d)

print (0.1+0.2==0.3)

val=id(d)
val1=id(val)
print(val, val1)

a=1.2
b=2
a , b = b , a 
print(id(a), a, id(b), b)
a=1.2 
b=2
print(id(a), a, id(b), b)