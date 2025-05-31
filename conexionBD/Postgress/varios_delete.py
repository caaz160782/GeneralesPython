from conexion_posgress import obtener_conexion

def eliminar_varios():
    try:
        entrada = input("🔹 Ingresa los id_persona a eliminar, separados por coma: ").strip()
        ids = [id.strip() for id in entrada.split(',') if id.strip().isdigit()]

        if not ids:
            print("⚠️ No se proporcionaron ID válidos.")
            return

        ids = tuple(map(int, ids))
        placeholders = ','.join(['%s'] * len(ids))
        sentencia = f"DELETE FROM persona WHERE id_persona IN ({placeholders})"

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sentencia, ids)
                conexion.commit()
                eliminados = cursor.rowcount

                if eliminados == 0:
                    print("ℹ️ No se eliminó ningún registro.")
                else:
                    print(f"✅ Registros eliminados: {eliminados}")

    except Exception as e:
        print(f"❌ Error al eliminar registros: {e}")

# Ejecutar
eliminar_varios()
