import logging as log
from datetime import datetime
import os

# Crear el nombre del archivo con la fecha actual
fecha_actual = datetime.now().strftime('%Y-%m-%d')
log_filename = f'capa_datos_{fecha_actual}.log'

# Asegurarte de que el directorio exista (opcional)
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_filepath = os.path.join(log_dir, log_filename)

# Configurar el formateador
formatter = log.Formatter(
    '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%I:%M:%S %p'
)

# Manejadores: archivo y consola
file_handler = log.FileHandler(log_filepath, encoding='utf-8')
file_handler.setFormatter(formatter)

stream_handler = log.StreamHandler()
stream_handler.setFormatter(formatter)

# Configurar logging
log.basicConfig(
    level=log.DEBUG,
    handlers=[file_handler, stream_handler]
)

# Ejemplo de uso
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')
