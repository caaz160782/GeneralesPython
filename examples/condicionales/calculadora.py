'''
Ejercicio 4:
Construir un programa que simule el funcionamiento de una calculadora que puede
realizar las cuatro operaciones aritméticas básicas (suma, resta, multiplicación
y división). El usuario debe especificar la operación con el primer carácter
del nombre de la operación.

S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División
'''

num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))

operacion = input("Digite la operacion: ").upper()

if operacion=='S':
    suma = num1+num2
    print(f"\nLa suma es: {suma}")
elif operacion == 'R':
    resta = num1-num2
    print(f"\nLa resta es: {resta}")
elif operacion=='M' or operacion=='P':
    mult = num1*num2
    print(f"\nLa multiplicación es: {mult:.2f}")
elif operacion=='D':
    div = num1/num2
    print(f"\nLa división es: {div:.2f}")
else:
    print("\nSe equivoco de operación")