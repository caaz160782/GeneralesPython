from conexion_posgress import obtener_conexion

def ejecutar_transaccion():
    try:
        with obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                conexion.autocommit = False

                sentencia_insert = (
                    "INSERT INTO persona (nombre, apellido, email) "
                    "VALUES (%s, %s, %s)"
                )
                valores_insert = ("Alex", "Rojas", "arojas@mail.com")
                cursor.execute(sentencia_insert, valores_insert)

                sentencia_update = (
                    "UPDATE persona "
                    "SET nombre=%s, apellido=%s, email=%s "
                    "WHERE id_persona=%s"
                )
                valores_update = ("Juan", "Perez", "jperez@mail.com", 201)
                cursor.execute(sentencia_update, valores_update)

                conexion.commit()
                print("Transacción completada y commit realizado.")

    except Exception as e:
        print("Ocurrió un error, se hizo rollback:", e)

if __name__ == "__main__":
    ejecutar_transaccion()
