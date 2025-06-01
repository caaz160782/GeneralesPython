from logger import log
import psycopg
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

class Conexion:
    _DATABASE = os.getenv('DB_NAME')
    _USERNAME = os.getenv('DB_USER')
    _PASSWORD = os.getenv('DB_PASSWORD')
    _DB_PORT = os.getenv('DB_PORT')
    _HOST = os.getenv('DB_HOST')

    @classmethod
    def obtener_conexion(cls):
        return psycopg.connect(
            host=cls._HOST,
            user=cls._USERNAME,
            password=cls._PASSWORD,
            port=cls._DB_PORT,
            dbname=cls._DATABASE
        )

if __name__ == '__main__':
    try:
        with Conexion.obtener_conexion() as conexion:
            log.debug(f'Conexión abierta exitosamente: {conexion.info.dsn}')
    except Exception as e:
        log.error(f'Error al conectar a la base de datos: {e}')
