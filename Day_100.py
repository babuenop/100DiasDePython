''' 
100 Dias De Python - Dia 100
---------------------------
Utiliza try para capturar e imprimir la excepcion dentro de la función y agrega el mensaje final utilizando finally 


'''

def dia100():
    try:
        mensaje="llegaste al último día"
        print(mensaje[len(mensaje)])
    except Exception as e:
        print("Error:{}".format(e))
    finally:
        print('Gracias @pythonlapaz Este reto ha terminado!!!') 
dia100()
