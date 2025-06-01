# menu/menu.py
from menu.persona_ops import menu_persona
from menu.cliente_ops import menu_cliente

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Personas")
    print("2. Clientes")
    print("0. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_persona()
        elif opcion == "2":
            menu_cliente()
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")
