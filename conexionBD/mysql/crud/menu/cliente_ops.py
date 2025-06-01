# menu/cliente_ops.py
from models.cliente import Cliente

cliente = Cliente()

def menu_cliente():
    while True:
        print("\n--- CLIENTES ---")
        print("1. Agregar")
        print("2. Mostrar")
        print("0. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            persona_id = input("ID de persona: ")
            empresa = input("Empresa: ")
            cliente.crear(persona_id, empresa)
        elif opcion == "2":
            clientes = cliente.leer_todos()
            for c in clientes:
                print(f"{c['id']}: persona_id={c['persona_id']}, empresa={c['empresa']}")
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")
