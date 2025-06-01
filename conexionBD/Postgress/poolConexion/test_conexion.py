import unittest
from conexion import Conexion
from logger_base import log

class TestConexion(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        Conexion.cerrar_pool()

    def test_pool_check(self):
        try:
            Conexion._pool.check()
            log.debug('✅ Pool verificado correctamente.')
        except Exception as e:
            self.fail(f'❌ Error al verificar el pool: {e}')

    def test_multiple_conexiones(self):
        try:
            for i in range(10):
                with Conexion.obtener_conexion() as conexion:
                    log.debug(f'🔁 Conexión #{i + 1} abierta y cerrada: id={id(conexion)}')
        except Exception as e:
            self.fail(f'❌ Error al obtener múltiples conexiones: {e}')

    def test_dummy(self):
        # Un test de relleno para ilustrar que aún puedes agregar más
        self.assertTrue(True)
