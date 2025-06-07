'''
Ejercicio 3:

Crear un programa que tenga una lista de clientes, cada cliente tiene su
Nombre, Apellido y DNI. El programa tendrá el siguiente menú de opciones:

1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir

PD: Cada opción de menú se realizará con una función
'''

def agregar_cliente(clientes,nombre,apellido,dni):
    cliente = {}
    cliente['nombre'] = nombre
    cliente['apellido'] = apellido
    cliente['dni'] = dni
    clientes.append(cliente)

def mostrar_clientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")

def mostrar_cliente(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")
            return True
    return False

def eliminar_cliente(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            clientes.remove(i)
            return True
    return False

clientes = [] # Creamos una lista

while True:
    print("""\t.:MENU:.
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir""")
    opcion = int(input("Digite una opción: "))

    print()

    if opcion==1:
        nombre = input("Nombre del cliente -> ")
        apellido = input("Apellido de cliente -> ")
        dni = input("DNI del cliente -> ")
        agregar_cliente(clientes,nombre,apellido,dni)

    elif opcion==2:
        mostrar_clientes(clientes)

    elif opcion==3:
        dni = input("DNI del cliente -> ")
        if mostrar_cliente(clientes,dni):
            print("Cliente encontrado")
        else:
            print("Cliente no encontrado")

    elif opcion==4:
        dni = input("DNI del cliente -> ")
        if eliminar_cliente(clientes,dni):
            print("Cliente eliminado")
        else:
            print("Cliente no encontrado")

    elif opcion==5:
        break

    else:
        print("Error, se equivocó de opción de menú")

    print()
