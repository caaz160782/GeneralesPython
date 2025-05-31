from conexion_posgress import obtener_conexion

def eliminar_persona():
    try:
        entrada = input("🔹 Proporciona el id_persona a eliminar: ").strip()
        if not entrada.isdigit():
            print("⚠️ El ID debe ser un número entero válido.")
            return

        id_persona = int(entrada)

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                sentencia = "DELETE FROM persona WHERE id_persona = %s"
                cursor.execute(sentencia, (id_persona,))
                conexion.commit()

                registros_eliminados = cursor.rowcount
                if registros_eliminados == 0:
                    print(f"ℹ️ No se encontró ningún registro con id_persona = {id_persona}.")
                else:
                    print(f"✅ Registro eliminado correctamente (id_persona = {id_persona}).")

    except Exception as e:
        print(f"❌ Error al eliminar el registro: {e}")

# Ejecutar
eliminar_persona()
