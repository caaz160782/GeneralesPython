from conexion_posgress import obtener_conexion  # Si estás usando un archivo separado para la conexión

def obtener_personas_por_ids():
    try:
        entrada = input("Proporciona los ID's a buscar (ej. 1,2,3): ").strip()

        if not entrada:
            print("⚠️ No ingresaste ningún ID.")
            return

        # Convertir la entrada a una lista de enteros, eliminando espacios
        ids = [int(id.strip()) for id in entrada.split(',') if id.strip().isdigit()]

        if not ids:
            print("⚠️ La lista de ID's no es válida.")
            return

        # Generar placeholders dinámicamente: %s, %s, %s...
        placeholders = ', '.join(['%s'] * len(ids))
        sentencia = f"SELECT * FROM persona WHERE id_persona IN ({placeholders})"

        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sentencia, ids)
                registros = cursor.fetchall()

                if registros:
                    for registro in registros:
                        print(registro)
                else:
                    print("🔍 No se encontraron resultados.")

    except Exception as e:
        print(f"❌ Error al consultar la base de datos: {e}")

# Ejecutar función
obtener_personas_por_ids()
