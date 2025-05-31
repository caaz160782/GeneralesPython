from conexion_posgress import obtener_conexion

try:
    with obtener_conexion() as conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM persona"
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for fila in registros:
                print(fila)
except Exception as e:
    print(f"❌ Ocurrió un error al consultar la base de datos: {e}")
