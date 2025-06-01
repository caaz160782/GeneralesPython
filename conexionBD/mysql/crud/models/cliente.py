# models/cliente.py
from db import get_connection
import logging

class Cliente:
    def crear(self, persona_id, empresa):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO clientes (persona_id, empresa) VALUES (%s, %s)",
                (persona_id, empresa)
            )
            conn.commit()
            logging.info(f"Cliente creado: persona_id={persona_id}")
        finally:
            cursor.close()
            conn.close()

    def leer_todos(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM clientes")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
