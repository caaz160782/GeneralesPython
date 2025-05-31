from conexion_posgress import obtener_conexion

def obtener_persona_por_id():
    try:
        id_persona = input("Proporciona el valor de id_persona: ").strip()

        if not id_persona.isdigit():
            print("⚠️ El valor debe ser un número entero.")
            return

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                sentencia = "SELECT * FROM persona WHERE id_persona = %s"
                cursor.execute(sentencia, (int(id_persona),))
                registro = cursor.fetchone()

                if registro:
                    print("✅ Registro encontrado:", registro)
                else:
                    print("🔍 No se encontró ninguna persona con ese ID.")

    except Exception as e:
        print(f"❌ Error al consultar la base de datos: {e}")

# Ejecutar
obtener_persona_por_id()

