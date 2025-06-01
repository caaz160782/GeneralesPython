from conexion_posgress import obtener_conexion

def insertar_multiples_personas():
    try:
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                sentencia = """
                    INSERT INTO persona (nombre, apellido, email)
                    VALUES (%s, %s, %s)
                """
                valores = [
                    ("Marcos", "Cantu", "mcantu@mail.com"),
                    ("Angel", "Quintana", "aquintana@mail.com"),
                    ("Maria", "Gonzalez", "mgonzalez@mail.com")
                ]

                cursor.executemany(sentencia, valores)
                conexion.commit()  # commit explícito, opcional con `with`

                registros_insertados = cursor.rowcount
                print(f"✅ Registros insertados: {registros_insertados}")

    except Exception as e:
        print(f"❌ Error al insertar registros: {e}")

# Ejecutar
insertar_multiples_personas()