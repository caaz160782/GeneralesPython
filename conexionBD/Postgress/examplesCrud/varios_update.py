from conexion_posgress import obtener_conexion 

def actualizar_multiples_personas():
    try:
        valores = [
            ("Juan", "Perez", "jperez@mail.com", 1),
            ("Ivonne", "Gutierrez", "igutierrez@mail.com", 2)
        ]

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                sentencia = """
                    UPDATE persona
                    SET nombre = %s, apellido = %s, email = %s
                    WHERE id_persona = %s
                """
                cursor.executemany(sentencia, valores)
                conexion.commit()

                registros_actualizados = cursor.rowcount
                print(f"✅ Registros actualizados: {registros_actualizados}")
    except Exception as e:
        print(f"❌ Error al actualizar registros: {e}")

# Ejecutar función
actualizar_multiples_personas()
