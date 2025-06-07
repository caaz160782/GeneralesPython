'''
Ejercicio 1: Desarrollar un programa que pueda calcular el valor del tipo
de cambio de moneda (de tu moneda – hacia dólar y viceversa).
'''

def cambio_Soles_Dolares(soles):
    return soles/3.3

def cambio_Dolares_Soles(dolares):
    return dolares*3.3

while True:
    print("""\t.:MENU:.
1. Convertir Soles a Dólares
2. Convertir de Dólares a Soles
3. Salir""")
    opcion = int(input("Digite una opcion: "))

    print()

    if opcion == 1:
        soles = float(input("Digite la cantidad de soles: "))
        print(f"Dólares -> ${cambio_Soles_Dolares(soles):.2f}")

    elif opcion==2:
        dolares = float(input("Digite la cantidad de dólares: "))
        print(f"Soles -> S/{cambio_Dolares_Soles(dolares):.2f}")

    elif opcion==3:
        break

    else:
        print("Se equivoco de opcion de opcion de menu")

    print()


