# Ejercicio 5 - Sumar digitos de un número

def sumarDigitos(num):
    if num==0: # Caso base
        resultado = 0
    else: # Caso recursivo
        resultado = sumarDigitos(int(num/10)) + (num%10)

    return resultado

valor = sumarDigitos(1114)
print(valor)

