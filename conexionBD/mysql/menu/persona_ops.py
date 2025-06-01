# menu/persona_ops.py
from models.persona import Persona

persona = Persona()

def menu_persona():
    while True:
        print("\n--- PERSONAS ---")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("0. Volver")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            correo = input("Correo: ")
            persona.crear(nombre, edad, correo)
        elif opcion == "2":
            personas = persona.leer_todos()
            for p in personas:
                print(f"{p['id']}: {p['nombre']}, {p['edad']} años, {p['correo']}")
        elif opcion == "3":
            idp = input("ID a actualizar: ")
            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            correo = input("Nuevo correo: ")
            persona.actualizar(idp, nombre, edad, correo)
        elif opcion == "4":
            idp = input("ID a eliminar: ")
            persona.eliminar(idp)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")
