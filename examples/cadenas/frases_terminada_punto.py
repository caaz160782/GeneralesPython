# Ejercicio 2 - Frase terminada en punto

cadena = input("Digite una cadena: ")

if cadena.endswith('.'): # Si el ultimo caracter de cadena es un punto
    print("La cadena finaliza con un punto")
else:
    print("La cadena no finaliza con un punto")