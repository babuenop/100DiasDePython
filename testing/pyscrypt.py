# import numpy as np
# import matplotlib.pyplot as plt
		

input_num = Element("how-many")
input16 = Element("input16")
input17 = Element("input17")
out = Element("outputDiv")
out16 = Element("out16")
out17 = Element("out17")

def random_num(n):
	"""
	"""
	r = np.random.normal(size=n)
	return np.array2string(r)

def clear(*ags, **kws):
	out = Element("outputDiv")
	out.clear()

def print_num(*ags, **kws):
	if input_num.value=='':
		n = 10
	else:
		n = int(input_num.value)
	r = random_num(n)
	out.write(f"Here are {n} random variates from Normal distribution: {r}")

def day16(*ags, **kws):
    var = input16.value
    out16.write(len(var))

def day17(*ags, **kws):
    var = input17.value
    out17.write(var.count('a'))

#Calcula el area del circulo     
def day25(*args, **kws):
    pi = 3.1416
    diameter = 3
    radius = diameter / 2
    area = pi * radius**2
    print(area)
    
    
 