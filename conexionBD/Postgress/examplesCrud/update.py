from conexion_posgress import obtener_conexion

def update_persona(nombre, apellido, email,id_persona):
    try:
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                sentencia = """
                            UPDATE persona
                            SET nombre = %s, apellido = %s, email = %s
                            WHERE id_persona = %s
                             """
                valores = (nombre, apellido, email,id_persona)
                cursor.execute(sentencia, valores)

                # Se puede usar explícitamente, aunque con `with` se hace automáticamente
                conexion.commit()

                registros_actualizados = cursor.rowcount
                print(f"✅ Registros insertados: {registros_actualizados}")
    except Exception as e:
        print(f"❌ Error al actualizar en la base de datos: {e}")

# Ejecutar ejemplo
update_persona("Carlos antonio", "zuñiga", "carlitos@email.com",1)
