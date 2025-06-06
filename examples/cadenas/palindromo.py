# Ejercicio 3 - Palabra o frase palíndroma

cadena = input("Digite una cadena: ")

# Primero, quitamos los espacios en blanco de la cadena
cadena = cadena.replace(" ","")

# Segundo, invertimos la cadena
cadena2 = cadena[::-1]

print(f"La cadena invertida es: {cadena2}")

if cadena == cadena2:
    print("La cadena es un palíndromo")
else:
    print("La cadena NO es un palíndromo")