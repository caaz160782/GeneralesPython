from logger_base import log
from psycopg_pool import ConnectionPool


class Conexion:
    _pool = ConnectionPool(
        conninfo="host=localhost port=5432 dbname=test_db_python user=root password=develop2024",
        min_size=1,
        max_size=5,
        timeout=5
    )

    @classmethod
    def obtener_conexion(cls):
        return cls._pool.connection()


if __name__ == '__main__':
    Conexion._pool.check()
    log.debug('Pool de conexiones verificado correctamente.')

    # Caso con with, donde se reutilizan las conexiones
    for i in range(10):  # Pide 10 conexiones, pero se liberan automáticamente
        with Conexion.obtener_conexion() as conexion:
            log.debug(f'Conexión #{i + 1} abierta y cerrada: id={id(conexion)}')

    Conexion._pool.close()
    log.debug('Pool de conexiones cerrado correctamente.')

    # Las conexiones de liberar de manera automatica al user with
    # y el metodo _pool.connection()