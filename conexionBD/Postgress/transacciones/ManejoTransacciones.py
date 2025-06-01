from conexion_posgress import obtener_conexion

def insertar_persona(nombre, apellido, email):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    conexion.autocommit = False
    try:
        sentencia = (
            "INSERT INTO persona (nombre, apellido, email) "
            "VALUES (%s, %s, %s)"
        )
        valores = (nombre, apellido, email)
        cursor.execute(sentencia, valores)
        conexion.commit()
        print("Transacción completada exitosamente")
    except Exception as e:
        conexion.rollback()
        print("Ocurrió un error. Se hizo rollback de la transacción:", e)
    finally:
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    insertar_persona("Maria", "Esparza", "mesparza@mail.com")
