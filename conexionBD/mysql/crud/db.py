
# db.py

import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv
from pathlib import Path

# === Cargar variables del archivo .envMysql ubicado en ../../.envMysql ===
env_path = Path(__file__).resolve().parents[2] / ".envMysql"
load_dotenv(dotenv_path=env_path)

DB_NAME = os.getenv("DB_NAME")

TABLES = {
    "personas": (
        "CREATE TABLE IF NOT EXISTS personas ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  nombre VARCHAR(100),"
        "  edad INT,"
        "  correo VARCHAR(100)"
        ")"
    ),
    "clientes": (
        "CREATE TABLE IF NOT EXISTS clientes ("
        "  id INT AUTO_INCREMENT PRIMARY KEY,"
        "  persona_id INT,"
        "  empresa VARCHAR(100),"
        "  FOREIGN KEY (persona_id) REFERENCES personas(id)"
        ")"
    )
}


def get_connection(database=True):
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME") if database else None
    )


def create_database_and_tables():
    conn = None
    cursor = None
    try:
        conn = get_connection(database=False)
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.execute(f"USE {DB_NAME}")

        for name, ddl in TABLES.items():
            cursor.execute(ddl)
        print("Base de datos y tablas creadas correctamente.")
    except Error as err:
        print(f"Error al crear la base de datos o tablas: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
