import os
from dotenv import load_dotenv
from psycopg_pool import ConnectionPool
from logger_base import log

# Cargar las variables de entorno del archivo .env
load_dotenv()

class Conexion:
    _pool = ConnectionPool(
        conninfo=(
            f"host={os.getenv('DB_HOST')} "
            f"port={os.getenv('DB_PORT')} "
            f"dbname={os.getenv('DB_NAME')} "
            f"user={os.getenv('DB_USER')} "
            f"password={os.getenv('DB_PASSWORD')}"
        ),
        min_size=1,
        max_size=5,
        timeout=5
    )

    @classmethod
    def obtener_conexion(cls):
        return cls._pool.connection()

    @classmethod
    def cerrar_pool(cls):
        cls._pool.close()
        log.debug('Pool de conexiones cerrado correctamente.')
