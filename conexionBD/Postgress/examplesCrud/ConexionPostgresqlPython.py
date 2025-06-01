import psycopg

try:
    conexion = psycopg.connect(
        user="root",
        password="develop2024",
        host="localhost",
        port="5432",
        dbname="test_db_python"
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM persona")
    registros = cursor.fetchall()
    print(registros)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()
