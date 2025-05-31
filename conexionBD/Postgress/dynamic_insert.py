from conexion_posgress import obtener_conexion

def insertar_personas_dinamicamente():
    try:
        personas = []

        print("🔵 Introduce datos de personas. Deja el nombre vacío para terminar.\n")

        while True:
            nombre = input("Nombre: ").strip()
            if not nombre:
                break

            apellido = input("Apellido: ").strip()
            email = input("Email: ").strip()

            if not apellido or not email:
                print("⚠️ Todos los campos son obligatorios. Intenta de nuevo.\n")
                continue

            personas.append((nombre, apellido, email))
            print("✅ Persona agregada.\n")

        if not personas:
            print("⚠️ No se ingresaron personas.")
            return

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                sentencia = """
                    INSERT INTO persona (nombre, apellido, email)
                    VALUES (%s, %s, %s)
                """
                cursor.executemany(sentencia, personas)
                conexion.commit()
                print(f"✅ Registros insertados: {cursor.rowcount}")

    except Exception as e:
        print(f"❌ Error al insertar personas: {e}")

# Ejecutar
insertar_personas_dinamicamente()
