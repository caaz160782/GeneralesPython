# models/persona.py
from db import get_connection
import logging

class Persona:
    def crear(self, nombre, edad, correo):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO personas (nombre, edad, correo) VALUES (%s, %s, %s)",
                (nombre, edad, correo)
            )
            conn.commit()
            logging.info(f"Persona creada: {nombre}")
        finally:
            cursor.close()
            conn.close()

    def leer_todos(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM personas")
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def actualizar(self, id, nombre, edad, correo):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE personas SET nombre=%s, edad=%s, correo=%s WHERE id=%s",
                (nombre, edad, correo, id)
            )
            conn.commit()
            logging.info(f"Persona actualizada: id={id}")
        finally:
            cursor.close()
            conn.close()

    def eliminar(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM personas WHERE id=%s", (id,))
            conn.commit()
            logging.info(f"Persona eliminada: id={id}")
        finally:
            cursor.close()
            conn.close()
