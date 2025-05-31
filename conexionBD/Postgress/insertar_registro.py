from conexion_posgress import obtener_conexion

def insertar_persona(nombre, apellido, email):
    try:
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                sentencia = """
                    INSERT INTO persona (nombre, apellido, email)
                    VALUES (%s, %s, %s)
                """
                valores = (nombre, apellido, email)
                cursor.execute(sentencia, valores)

                # Se puede usar explícitamente, aunque con `with` se hace automáticamente
                conexion.commit()

                registros_insertados = cursor.rowcount
                print(f"✅ Registros insertados: {registros_insertados}")
    except Exception as e:
        print(f"❌ Error al insertar en la base de datos: {e}")

# Ejecutar ejemplo
insertar_persona("Carlos", "Lara", "clara@mail.com")
