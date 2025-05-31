try:
    archivo = open('prueba.txt', 'w')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('sin codificacion')
except Exception as e:
    print(e)
finally:
    archivo.close()