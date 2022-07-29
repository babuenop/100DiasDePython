''' 
100 Dias De Python - Dia 98
---------------------------
Utiliza try para capturar e imprimir la excepcion de una division entre 0 del siguiente fragmento de codigo 

'''
import traceback
a = 7

try:
    b= a/00
except Exception:
    traceback.print_exc()
else:
  print("Nothing went wrong")

