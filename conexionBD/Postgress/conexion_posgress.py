import psycopg
import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

def obtener_conexion():
    return psycopg.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME")
    )
